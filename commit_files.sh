#!/bin/bash

echo "Adding 67 protocol files to git..."
git add protocol_files/

echo "Committing files..."
git commit -m "Add 67 individual protocol files split from consolidated gists.md

- Processed consolidated auditor descriptions from gists.md
- Split into individual protocol-specific markdown files  
- Includes files like: stylus.md, incentiv.md, chronicle.md, starknet.md, etc.
- Total: 67 protocol files with auditor descriptions"

echo "Pushing to GitHub..."
git push origin main

echo "Done! Files should now be available on GitHub."