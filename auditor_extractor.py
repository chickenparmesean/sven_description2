#!/usr/bin/env python3
"""
Auditor Description Extractor

This script processes markdown files from a GitHub repository and extracts
individual auditor descriptions while preserving protocol names from filenames.

Usage:
    python auditor_extractor.py --repo chickenparmesean/descriptions
"""

import os
import re
import json
import csv
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from collections import defaultdict, Counter
import requests
from urllib.parse import quote


class GitHubAuditorExtractor:
    """Extracts auditor descriptions from GitHub repository markdown files."""
    
    def __init__(self, token: str):
        """
        Initialize the extractor with GitHub token.
        
        Args:
            token: GitHub personal access token
        """
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Auditor-Extractor/1.0'
        }
        self.auditor_data = []
        self.duplicate_analysis = defaultdict(list)
        
    def extract_protocol_name(self, filename: str) -> str:
        """
        Extract protocol name from filename by removing hash and extension.
        
        Args:
            filename: Full filename like 'Vols fi 24d06b22cd1c80a4aefaebec720fdc74.md'
            
        Returns:
            Protocol name like 'Vols fi'
        """
        # Remove .md extension
        name_without_ext = filename.replace('.md', '')
        
        # Remove hash pattern (space + 32 hex characters)
        hash_pattern = r'\s+[a-f0-9]{32}$'
        protocol_name = re.sub(hash_pattern, '', name_without_ext)
        
        return protocol_name.strip()
    
    def fetch_repository_contents(self, repo: str, path: str = "") -> List[Dict]:
        """
        Fetch repository contents using GitHub API.
        
        Args:
            repo: Repository name like 'owner/repo'
            path: Path within repo (empty for root)
            
        Returns:
            List of file/directory information
        """
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
            
        except requests.RequestException as e:
            print(f"Error fetching repository contents: {e}")
            if response.status_code == 404:
                print(f"Repository '{repo}' not found or access denied")
            elif response.status_code == 401:
                print("Authentication failed - check your GitHub token")
            raise
    
    def fetch_file_content(self, repo: str, file_path: str) -> str:
        """
        Fetch individual file content using GitHub API.
        
        Args:
            repo: Repository name like 'owner/repo'
            file_path: Path to file in repository
            
        Returns:
            File content as string
        """
        # URL encode the file path
        encoded_path = quote(file_path, safe='/')
        url = f"https://api.github.com/repos/{repo}/contents/{encoded_path}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            file_info = response.json()
            
            if file_info.get('encoding') == 'base64':
                import base64
                content = base64.b64decode(file_info['content']).decode('utf-8')
                return content
            else:
                print(f"Warning: Unexpected encoding for {file_path}")
                return ""
                
        except requests.RequestException as e:
            print(f"Error fetching file {file_path}: {e}")
            return ""
    
    def parse_markdown_auditors(self, content: str, protocol: str) -> List[Dict[str, str]]:
        """
        Parse markdown content to extract auditor descriptions.
        
        Args:
            content: Markdown file content
            protocol: Protocol name from filename
            
        Returns:
            List of auditor data dictionaries
        """
        auditors = []
        lines = content.split('\n')
        current_auditor = None
        current_description = []
        
        # Patterns for auditor headers
        header_patterns = [
            r'^#+\s*([^#\n]+)$',  # Any level header
            r'^\*\*([^*]+)\*\*$', # Bold text on its own line
        ]
        
        for line in lines:
            line = line.strip()
            
            # Check if this line is an auditor header
            is_header = False
            auditor_name = None
            
            for pattern in header_patterns:
                match = re.match(pattern, line)
                if match:
                    auditor_name = match.group(1).strip()
                    # Filter out common section headers that aren't auditor names
                    if not self.is_section_header(auditor_name):
                        is_header = True
                        break
            
            if is_header and auditor_name:
                # Save previous auditor if exists
                if current_auditor and current_description:
                    description_text = '\n'.join(current_description).strip()
                    if description_text:
                        auditors.append({
                            'protocol': protocol,
                            'auditor': current_auditor,
                            'description': description_text
                        })
                
                # Start new auditor
                current_auditor = auditor_name
                current_description = []
                
            elif current_auditor and line:
                # Add content to current auditor description
                # Skip markdown headers and horizontal rules
                if not re.match(r'^#{1,6}\s', line) and line != '---':
                    current_description.append(line)
        
        # Save last auditor
        if current_auditor and current_description:
            description_text = '\n'.join(current_description).strip()
            if description_text:
                auditors.append({
                    'protocol': protocol,
                    'auditor': current_auditor,
                    'description': description_text
                })
        
        return auditors
    
    def is_section_header(self, text: str) -> bool:
        """
        Check if text is likely a section header rather than auditor name.
        
        Args:
            text: Header text to check
            
        Returns:
            True if likely a section header
        """
        section_keywords = [
            'overview', 'introduction', 'background', 'summary', 'description',
            'watsons', 'auditors', 'team', 'researchers', 'security', 'experience',
            'achievements', 'why they are a good fit', 'fit', 'recommendation',
            'about', 'profile', 'details', 'history', 'expertise'
        ]
        
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in section_keywords)
    
    def process_repository(self, repo: str) -> None:
        """
        Process all markdown files in the repository.
        
        Args:
            repo: Repository name like 'owner/repo'
        """
        print(f"Processing repository: {repo}")
        
        try:
            contents = self.fetch_repository_contents(repo)
            md_files = [item for item in contents if item['name'].endswith('.md')]
            
            print(f"Found {len(md_files)} markdown files")
            
            for file_info in md_files:
                filename = file_info['name']
                protocol = self.extract_protocol_name(filename)
                
                print(f"Processing: {filename} → Protocol: {protocol}")
                
                content = self.fetch_file_content(repo, filename)
                if content:
                    auditors = self.parse_markdown_auditors(content, protocol)
                    self.auditor_data.extend(auditors)
                    
                    # Track for duplicate analysis
                    for auditor in auditors:
                        auditor_name = auditor['auditor']
                        self.duplicate_analysis[auditor_name.lower()].append({
                            'original_name': auditor_name,
                            'protocol': protocol
                        })
                    
                    print(f"  Extracted {len(auditors)} auditors")
                else:
                    print(f"  Warning: Could not fetch content for {filename}")
            
            print(f"\nTotal auditors extracted: {len(self.auditor_data)}")
            
        except Exception as e:
            print(f"Error processing repository: {e}")
            raise
    
    def generate_json_output(self, output_path: str = "auditor-data.json") -> None:
        """Generate JSON output file."""
        print(f"Generating {output_path}...")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.auditor_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Generated {output_path} with {len(self.auditor_data)} entries")
    
    def generate_csv_output(self, output_path: str = "auditor-data.csv") -> None:
        """Generate CSV output file for Excel/Google Sheets editing."""
        print(f"Generating {output_path}...")
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['protocol', 'auditor', 'description'])
            writer.writeheader()
            writer.writerows(self.auditor_data)
        
        print(f"✓ Generated {output_path} with {len(self.auditor_data)} entries")
    
    def generate_html_report(self, output_path: str = "auditor-report.html") -> None:
        """Generate HTML report with sorting and filtering."""
        print(f"Generating {output_path}...")
        
        protocols = sorted(set(item['protocol'] for item in self.auditor_data))
        auditors = sorted(set(item['auditor'] for item in self.auditor_data))
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditor Descriptions Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 30px;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #007acc;
            padding-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 6px;
            border-left: 4px solid #007acc;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #007acc;
        }}
        .filters {{
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 15px;
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 6px;
        }}
        select, input {{
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        button {{
            padding: 8px 16px;
            background: #007acc;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }}
        button:hover {{
            background: #005fa3;
        }}
        .auditor-card {{
            border: 1px solid #e1e5e9;
            border-radius: 6px;
            margin: 15px 0;
            background: white;
        }}
        .auditor-header {{
            background: #f8f9fa;
            padding: 15px 20px;
            border-bottom: 1px solid #e1e5e9;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .auditor-name {{
            font-weight: bold;
            color: #333;
            font-size: 1.1em;
        }}
        .protocol-tag {{
            background: #007acc;
            color: white;
            padding: 4px 8px;
            border-radius: 3px;
            font-size: 0.85em;
        }}
        .auditor-description {{
            padding: 20px;
            line-height: 1.6;
            white-space: pre-wrap;
        }}
        .no-results {{
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 40px;
        }}
        .count {{
            color: #666;
            font-size: 0.9em;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Auditor Descriptions Report</h1>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{len(self.auditor_data)}</div>
                <div>Total Auditors</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(protocols)}</div>
                <div>Protocols</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(auditors)}</div>
                <div>Unique Auditor Names</div>
            </div>
        </div>
        
        <div class="filters">
            <select id="protocolFilter">
                <option value="">All Protocols</option>
                {''.join(f'<option value="{protocol}">{protocol}</option>' for protocol in protocols)}
            </select>
            <input type="text" id="auditorSearch" placeholder="Search auditors...">
            <button onclick="clearFilters()">Clear Filters</button>
        </div>
        
        <div class="count" id="resultCount"></div>
        
        <div id="auditorList">
            {''.join(self._generate_auditor_card(item) for item in self.auditor_data)}
        </div>
        
        <div id="noResults" class="no-results" style="display: none;">
            No auditors match your current filters.
        </div>
    </div>
    
    <script>
        const auditorData = {json.dumps(self.auditor_data, ensure_ascii=False)};
        
        function filterAuditors() {{
            const protocolFilter = document.getElementById('protocolFilter').value.toLowerCase();
            const auditorSearch = document.getElementById('auditorSearch').value.toLowerCase();
            
            const filtered = auditorData.filter(item => {{
                const matchesProtocol = !protocolFilter || item.protocol.toLowerCase() === protocolFilter;
                const matchesAuditor = !auditorSearch || 
                    item.auditor.toLowerCase().includes(auditorSearch) ||
                    item.description.toLowerCase().includes(auditorSearch);
                return matchesProtocol && matchesAuditor;
            }});
            
            updateDisplay(filtered);
        }}
        
        function updateDisplay(filtered) {{
            const auditorList = document.getElementById('auditorList');
            const noResults = document.getElementById('noResults');
            const resultCount = document.getElementById('resultCount');
            
            if (filtered.length === 0) {{
                auditorList.style.display = 'none';
                noResults.style.display = 'block';
                resultCount.textContent = 'No results found';
            }} else {{
                auditorList.innerHTML = filtered.map(item => 
                    `<div class="auditor-card">
                        <div class="auditor-header">
                            <div class="auditor-name">${{item.auditor}}</div>
                            <div class="protocol-tag">${{item.protocol}}</div>
                        </div>
                        <div class="auditor-description">${{item.description}}</div>
                    </div>`
                ).join('');
                auditorList.style.display = 'block';
                noResults.style.display = 'none';
                resultCount.textContent = `Showing ${{filtered.length}} of ${{auditorData.length}} auditors`;
            }}
        }}
        
        function clearFilters() {{
            document.getElementById('protocolFilter').value = '';
            document.getElementById('auditorSearch').value = '';
            updateDisplay(auditorData);
        }}
        
        document.getElementById('protocolFilter').addEventListener('change', filterAuditors);
        document.getElementById('auditorSearch').addEventListener('input', filterAuditors);
        
        // Initialize display
        updateDisplay(auditorData);
    </script>
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Generated {output_path} with interactive filtering")
    
    def _generate_auditor_card(self, item: Dict[str, str]) -> str:
        """Generate HTML for a single auditor card."""
        return f"""
        <div class="auditor-card">
            <div class="auditor-header">
                <div class="auditor-name">{item['auditor']}</div>
                <div class="protocol-tag">{item['protocol']}</div>
            </div>
            <div class="auditor-description">{item['description']}</div>
        </div>"""
    
    def generate_duplicate_analysis(self, output_path: str = "duplicate-analysis.txt") -> None:
        """Generate duplicate analysis report."""
        print(f"Generating {output_path}...")
        
        duplicates_found = []
        similar_names = []
        
        # Find exact duplicates and similar names
        for normalized_name, instances in self.duplicate_analysis.items():
            if len(instances) > 1:
                original_names = [inst['original_name'] for inst in instances]
                unique_names = set(original_names)
                
                if len(unique_names) == 1:
                    # Same name across multiple protocols
                    duplicates_found.append({
                        'name': instances[0]['original_name'],
                        'protocols': [inst['protocol'] for inst in instances],
                        'count': len(instances)
                    })
                else:
                    # Similar names (different capitalization/formatting)
                    similar_names.append({
                        'variations': list(unique_names),
                        'protocols': [inst['protocol'] for inst in instances]
                    })
        
        # Generate report
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("AUDITOR DUPLICATE ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"Total unique auditor entries: {len(self.auditor_data)}\n")
            f.write(f"Unique normalized names: {len(self.duplicate_analysis)}\n\n")
            
            if duplicates_found:
                f.write("EXACT DUPLICATES (Same auditor across multiple protocols):\n")
                f.write("-" * 60 + "\n")
                for dup in sorted(duplicates_found, key=lambda x: x['count'], reverse=True):
                    f.write(f"• {dup['name']} ({dup['count']} times)\n")
                    f.write(f"  Protocols: {', '.join(dup['protocols'])}\n\n")
            else:
                f.write("No exact duplicates found.\n\n")
            
            if similar_names:
                f.write("SIMILAR NAMES (Potential formatting variations):\n")
                f.write("-" * 60 + "\n")
                for sim in similar_names:
                    f.write(f"• Variations: {', '.join(sim['variations'])}\n")
                    f.write(f"  Protocols: {', '.join(sim['protocols'])}\n\n")
            else:
                f.write("No similar name variations found.\n\n")
            
            # Most common auditors
            auditor_counts = Counter(item['auditor'] for item in self.auditor_data)
            f.write("MOST FREQUENT AUDITORS:\n")
            f.write("-" * 30 + "\n")
            for auditor, count in auditor_counts.most_common(20):
                f.write(f"• {auditor}: {count} protocols\n")
        
        print(f"✓ Generated {output_path} with duplicate analysis")
        print(f"  Found {len(duplicates_found)} exact duplicates")
        print(f"  Found {len(similar_names)} similar name groups")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract auditor descriptions from GitHub repository markdown files"
    )
    parser.add_argument(
        '--repo',
        required=True,
        help='GitHub repository (e.g., owner/repo-name)'
    )
    parser.add_argument(
        '--output-dir',
        default='.',
        help='Output directory for generated files (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Get GitHub token from environment
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("Please set your GitHub personal access token as GITHUB_TOKEN")
        return 1
    
    try:
        # Create output directory
        output_dir = Path(args.output_dir)
        output_dir.mkdir(exist_ok=True)
        
        # Initialize extractor
        extractor = GitHubAuditorExtractor(token)
        
        # Process repository
        extractor.process_repository(args.repo)
        
        if not extractor.auditor_data:
            print("Warning: No auditor data extracted. Check repository contents and markdown format.")
            return 1
        
        # Generate all output formats
        extractor.generate_json_output(output_dir / "auditor-data.json")
        extractor.generate_csv_output(output_dir / "auditor-data.csv")
        extractor.generate_html_report(output_dir / "auditor-report.html")
        extractor.generate_duplicate_analysis(output_dir / "duplicate-analysis.txt")
        
        print(f"\n✅ Successfully processed {len(extractor.auditor_data)} auditor descriptions")
        print(f"📁 Files generated in: {output_dir.absolute()}")
        print("📊 Open auditor-report.html in your browser for interactive viewing")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())