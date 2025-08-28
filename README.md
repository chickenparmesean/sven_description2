# Auditor Description Splitter

A Python script that splits consolidated auditor descriptions from a GitHub repository into individual protocol markdown files.

## Overview

This script processes a consolidated file (like `gists.md`) that contains multiple auditor descriptions organized under section headers. It identifies section markers that start with `**From ./` and end with `.md**`, extracts protocol names from the filenames, and creates separate markdown files for each protocol.

## Features

- ✅ Fetches files from GitHub URLs or reads local files
- ✅ Parses section markers using robust regular expressions
- ✅ Extracts protocol names from filename paths
- ✅ Creates individual `.md` files named after each protocol
- ✅ Handles duplicate protocol names automatically
- ✅ Preserves markdown formatting
- ✅ Provides detailed console output and error handling
- ✅ Supports both remote URLs and local files

## Installation

No additional dependencies required beyond Python's standard library and `requests`:

```bash
pip install requests
