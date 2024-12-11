import os
import argparse
from urllib.parse import unquote
import re

def format_date_title(filename):
    # Remove .md and convert underscores to hyphens
    return filename.replace('.md', '').replace('_', '-')

def format_page_title(filename):
    # Remove .md and decode URL encoding
    return unquote(filename.replace('.md', ''))

def read_and_format_file(filepath, title):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        formatted_content = f"""
---------
{title}
---------

{content}

"""
        return formatted_content
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return ""

def main():
    parser = argparse.ArgumentParser(description='Combine Logseq files into a single markdown file')
    parser.add_argument('folder', help='Root folder containing journals and pages folders')
    args = parser.parse_args()

    # Initialize output content with journals first
    output_content = []
    
    # Process journals
    journals_path = os.path.join(args.folder, 'journals')
    if os.path.exists(journals_path):
        journal_files = sorted([f for f in os.listdir(journals_path) if f.endswith('.md')])
        for filename in journal_files:
            filepath = os.path.join(journals_path, filename)
            title = format_date_title(filename)
            content = read_and_format_file(filepath, title)
            output_content.append(content)

    # Process pages
    pages_path = os.path.join(args.folder, 'pages')
    if os.path.exists(pages_path):
        page_files = sorted([f for f in os.listdir(pages_path) if f.endswith('.md')])
        for filename in page_files:
            filepath = os.path.join(pages_path, filename)
            title = format_page_title(filename)
            content = read_and_format_file(filepath, title)
            output_content.append(content)

    # Write combined content to life.md in the current directory
    output_file = 'life.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(output_content))
    
    print(f"Combined files have been written to {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()