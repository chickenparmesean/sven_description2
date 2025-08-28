#!/usr/bin/env python3
"""
GitHub Auditor Description Splitter

This script reads a consolidated gists.md file containing auditor descriptions
and splits them into individual protocol markdown files based on section markers.

Usage:
    python split_auditor_descriptions.py [--url URL] [--input FILE] [--output DIR]
"""

import os
import re
import sys
import argparse
from pathlib import Path
from urllib.parse import urlparse
import requests
from typing import List, Tuple, Optional


class AuditorDescriptionSplitter:
    """Handles splitting of consolidated auditor descriptions into individual files."""
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the splitter.
        
        Args:
            output_dir: Directory to save the split files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Pattern to match section markers like "# From ./path/filename.md"
        self.marker_pattern = re.compile(
            r'^# From \./(.+/)?([^/]+)\.md$',
            re.MULTILINE
        )
    
    def fetch_content_from_url(self, url: str) -> str:
        """
        Fetch content from a GitHub URL.
        
        Args:
            url: GitHub URL to fetch content from
            
        Returns:
            Content of the file as string
            
        Raises:
            requests.RequestException: If unable to fetch content
        """
        print(f"Fetching content from: {url}")
        
        # Convert GitHub blob URL to raw URL if needed
        if "github.com" in url and "/blob/" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            print(f"Converting to raw URL: {raw_url}")
            url = raw_url
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            if response.status_code == 404:
                raise requests.RequestException(f"File not found (404) at URL: {url}")
            
            content = response.text
            print(f"Successfully fetched {len(content)} characters")
            return content
            
        except requests.RequestException as e:
            print(f"Error fetching content from URL: {e}")
            raise
    
    def read_local_file(self, file_path: str) -> str:
        """
        Read content from a local file.
        
        Args:
            file_path: Path to the local file
            
        Returns:
            Content of the file as string
            
        Raises:
            FileNotFoundError: If file doesn't exist
            IOError: If unable to read file
        """
        print(f"Reading local file: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"Successfully read {len(content)} characters from local file")
            return content
            
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            raise
        except IOError as e:
            print(f"Error reading file: {e}")
            raise
    
    def parse_sections(self, content: str) -> List[Tuple[str, str]]:
        """
        Parse the content and extract sections based on markers.
        
        Args:
            content: The full content to parse
            
        Returns:
            List of tuples containing (protocol_name, section_content)
        """
        print("Parsing content for section markers...")
        
        sections = []
        marker_matches = list(self.marker_pattern.finditer(content))
        
        if not marker_matches:
            print("Warning: No section markers found in the content")
            return sections
        
        print(f"Found {len(marker_matches)} section markers")
        
        for i, match in enumerate(marker_matches):
            # Extract protocol name from filename (group 2 from our regex)
            protocol_name = match.group(2)
            
            if not protocol_name:
                print(f"Warning: Could not extract filename from marker: {match.group(0)}")
                continue
            
            # Find the start and end positions for this section
            section_start = match.end()
            
            # If this is the last section, go to end of content
            if i == len(marker_matches) - 1:
                section_end = len(content)
            else:
                # Otherwise, go to the start of the next marker
                section_end = marker_matches[i + 1].start()
            
            # Extract the content between markers
            section_content = content[section_start:section_end].strip()
            
            if section_content:
                sections.append((protocol_name, section_content))
                print(f"Extracted section for protocol: {protocol_name} ({len(section_content)} characters)")
            else:
                print(f"Warning: Empty content for protocol: {protocol_name}")
        
        return sections
    
    def handle_duplicate_names(self, sections: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """
        Handle duplicate protocol names by appending numbers.
        
        Args:
            sections: List of (protocol_name, content) tuples
            
        Returns:
            List of (unique_protocol_name, content) tuples
        """
        seen_names = {}
        unique_sections = []
        
        for protocol_name, content in sections:
            original_name = protocol_name
            counter = 1
            
            # Keep incrementing until we find a unique name
            while protocol_name in seen_names:
                protocol_name = f"{original_name}_{counter}"
                counter += 1
            
            seen_names[protocol_name] = True
            unique_sections.append((protocol_name, content))
            
            if protocol_name != original_name:
                print(f"Renamed duplicate protocol: {original_name} -> {protocol_name}")
        
        return unique_sections
    
    def save_sections(self, sections: List[Tuple[str, str]]) -> None:
        """
        Save each section to its own markdown file.
        
        Args:
            sections: List of (protocol_name, content) tuples
        """
        print(f"\nSaving {len(sections)} protocol files to: {self.output_dir}")
        
        # Handle duplicate names
        unique_sections = self.handle_duplicate_names(sections)
        
        saved_count = 0
        
        for protocol_name, content in unique_sections:
            # Clean protocol name for filename
            safe_filename = re.sub(r'[^\w\-_]', '_', protocol_name)
            file_path = self.output_dir / f"{safe_filename}.md"
            
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✓ Saved: {file_path}")
                saved_count += 1
                
            except IOError as e:
                print(f"✗ Error saving {file_path}: {e}")
        
        print(f"\nSuccessfully saved {saved_count} protocol files")
    
    def split_file(self, source: str, is_url: bool = True) -> None:
        """
        Main method to split the auditor descriptions file.
        
        Args:
            source: URL or file path to the source file
            is_url: Whether source is a URL or local file path
        """
        try:
            # Get content
            if is_url:
                content = self.fetch_content_from_url(source)
            else:
                content = self.read_local_file(source)
            
            if not content.strip():
                print("Error: Source file is empty")
                return
            
            # Parse sections
            sections = self.parse_sections(content)
            
            if not sections:
                print("No valid sections found to split")
                return
            
            # Save sections
            self.save_sections(sections)
            
        except Exception as e:
            print(f"Error processing file: {e}")
            sys.exit(1)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Split consolidated auditor descriptions into individual protocol files"
    )
    
    # Add mutually exclusive group for input source
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument(
        '--url',
        help='GitHub URL to fetch the gists.md file from'
    )
    source_group.add_argument(
        '--input',
        help='Local path to the gists.md file'
    )
    
    parser.add_argument(
        '--output',
        default='output',
        help='Output directory for split files (default: output)'
    )
    
    args = parser.parse_args()
    
    # Create splitter instance
    splitter = AuditorDescriptionSplitter(args.output)
    
    # Process the file
    if args.url:
        print(f"Processing URL: {args.url}")
        splitter.split_file(args.url, is_url=True)
    else:
        print(f"Processing local file: {args.input}")
        splitter.split_file(args.input, is_url=False)


if __name__ == "__main__":
    main()
