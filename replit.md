# Auditor Description Splitter

## Overview

A Python command-line tool that processes consolidated auditor description files and splits them into individual protocol-specific markdown files. The tool is designed to parse files containing multiple auditor descriptions organized under section headers, extracting each section into separate files based on protocol names derived from file paths.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Application Structure
- **Single-file architecture**: The entire application is contained in `split_auditor_descriptions.py`, following a simple script-based approach suitable for command-line utilities
- **Class-based design**: Uses `AuditorDescriptionSplitter` class to encapsulate all functionality, providing clean separation of concerns
- **Standard library focus**: Relies primarily on Python's built-in libraries with minimal external dependencies

### Data Processing Pipeline
- **Input handling**: Supports both remote GitHub URLs and local file inputs through a unified interface
- **Pattern matching**: Uses regular expressions to identify section markers in the format `**From ./path/filename.md**`
- **Content extraction**: Parses sections between markers and extracts protocol names from file paths
- **File generation**: Creates individual markdown files named after extracted protocol names with automatic duplicate handling

### Error Handling Strategy
- **Graceful degradation**: Continues processing even when individual sections fail
- **Detailed logging**: Provides comprehensive console output for debugging and monitoring
- **Input validation**: Validates URLs, file paths, and content before processing

### File Management
- **Automatic directory creation**: Creates output directories as needed
- **Duplicate handling**: Automatically handles naming conflicts for duplicate protocol names
- **Path abstraction**: Uses `pathlib.Path` for cross-platform file system operations

## External Dependencies

### Required Libraries
- **requests**: HTTP client library for fetching content from GitHub URLs
- **Python Standard Library**: 
  - `os`, `sys` for system operations
  - `re` for regular expression pattern matching
  - `argparse` for command-line argument parsing
  - `pathlib` for modern path handling
  - `urllib.parse` for URL parsing
  - `typing` for type hints

### Supported Input Sources
- **GitHub repositories**: Direct URL support for fetching consolidated files
- **Local file system**: Support for processing local markdown files
- **Output formats**: Generates standard markdown (.md) files compatible with any markdown processor