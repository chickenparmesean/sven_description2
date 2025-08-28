#!/bin/bash

echo "Adding auditor analysis files to git..."

# Add all the generated auditor files
git add auditor-data.json
git add auditor-data.csv  
git add auditor-report.html
git add duplicate-analysis.txt
git add auditor_extractor.py

echo "Committing files..."
git commit -m "Add comprehensive auditor analysis files

- auditor-data.json: 942 auditor descriptions in structured JSON format
- auditor-data.csv: Excel/Google Sheets compatible format for editing
- auditor-report.html: Interactive web report with filtering and sorting
- duplicate-analysis.txt: Analysis of duplicate names and variations
- auditor_extractor.py: Script for processing GitHub markdown files

Processed 165 markdown files from private repository
Extracted protocol names and linked to individual auditor descriptions"

echo "Pushing to GitHub..."
git push origin main

echo "✅ Done! Auditor analysis files are now saved to GitHub."