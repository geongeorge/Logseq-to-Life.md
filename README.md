# Logseq to Life

Turn your Logseq journals and notes into a single markdown file you can use to chat with AI about your life journey. Perfect for reflecting on your past entries, finding patterns in your thoughts, or getting AI-powered insights about your personal growth.

Use in Claude projects or custom GPT in ChatGPT

## Why Use This?

- **Chat About Your Life**: Upload the combined file to Claude or other AI assistants to have meaningful conversations about your journals and notes
- **Personal Growth**: Get AI-powered insights about patterns in your thinking and personal development
- **Easy Memory Access**: Instead of searching through separate files, have all your thoughts in one place
- **Private**: Process your files locally - the script runs on your computer, you control what you share

## Features

- Combines all markdown files from Logseq journals and pages folders
- Formats journal dates (e.g., 2022_05_15 → 2022-05-15)
- Decodes URL-encoded page titles (e.g., "Case Study%3A Example" → "Case Study: Example")
- Maintains chronological order for journal entries
- Places journal entries before pages in the output
- Creates output file in the current working directory
- Supports UTF-8 encoding

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository

## Usage

Run the script from the command line:

```bash
python app.py /path/to/logseq/folder
```
