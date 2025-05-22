#!/usr/bin/env python3

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def extract_frontmatter_and_title(file_path):
    """Extract frontmatter and title from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with frontmatter
        if content.startswith('---'):
            # Split frontmatter from content
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_str = parts[1].strip()
                remaining_content = parts[2].strip()
                
                try:
                    frontmatter = yaml.safe_load(frontmatter_str)
                    title = frontmatter.get('title', '')
                    date = frontmatter.get('date', '')
                    
                    # If no title in frontmatter, look for first heading
                    if not title and remaining_content:
                        heading_match = re.search(r'^#\s+(.+)$', remaining_content, re.MULTILINE)
                        if heading_match:
                            title = heading_match.group(1).strip()
                    
                    return title, date, frontmatter
                except yaml.YAMLError:
                    pass
        
        # If no frontmatter, look for first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = heading_match.group(1).strip() if heading_match else ''
        
        return title, '', {}
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return '', '', {}

def extract_date_from_filename(filename):
    """Extract date from filename in format YYYY-MM-DD."""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else None

def get_relative_path(file_path, docs_dir):
    """Get relative path from docs directory."""
    return os.path.relpath(file_path, docs_dir)

def main():
    docs_dir = "/mnt/c/Users/jackc/git/mkdocs-material-test/docs"
    
    # Get all markdown files excluding specified ones
    excluded_files = {'archive.md', 'tags.md', 'index.md', '404.md'}
    
    files_data = []
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md') and file not in excluded_files:
                file_path = os.path.join(root, file)
                relative_path = get_relative_path(file_path, docs_dir)
                
                # Skip if it's an index.md file
                if file == 'index.md':
                    continue
                
                title, frontmatter_date, frontmatter = extract_frontmatter_and_title(file_path)
                filename_date = extract_date_from_filename(file)
                
                # Use frontmatter date if available, otherwise filename date
                date = frontmatter_date or filename_date
                
                # If no title found, use filename without date and extension
                if not title:
                    title = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', file).replace('.md', '').replace('-', ' ').replace('_', ' ')
                
                files_data.append({
                    'path': relative_path,
                    'filename': file,
                    'title': title,
                    'date': date,
                    'frontmatter': frontmatter
                })
    
    # Sort by date (put files without dates at the end)
    files_data.sort(key=lambda x: (x['date'] or '9999-99-99', x['filename']))
    
    # Group by year and month
    grouped = defaultdict(lambda: defaultdict(list))
    no_date_files = []
    
    for file_data in files_data:
        if file_data['date']:
            try:
                date_obj = datetime.strptime(file_data['date'], '%Y-%m-%d')
                year = date_obj.year
                month = date_obj.strftime('%B')  # Full month name
                grouped[year][month].append(file_data)
            except ValueError:
                no_date_files.append(file_data)
        else:
            no_date_files.append(file_data)
    
    # Generate archive content
    archive_content = """---
title: Archive
description: Chronological archive of all content
---

# Archive

This page provides a chronological listing of all content in the digital garden, organized by year and month.

"""
    
    # Sort years in descending order
    for year in sorted(grouped.keys(), reverse=True):
        archive_content += f"## {year}\n\n"
        
        # Sort months chronologically within each year
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        
        year_months = grouped[year]
        sorted_months = sorted(year_months.keys(), key=lambda x: month_order.index(x) if x in month_order else 12)
        
        for month in sorted_months:
            archive_content += f"### {month}\n"
            
            # Sort files within month by date
            month_files = sorted(year_months[month], key=lambda x: x['date'])
            
            for file_data in month_files:
                title = file_data['title']
                path = file_data['path']
                
                # Get description from frontmatter if available
                description = ""
                if 'description' in file_data['frontmatter']:
                    description = f" - {file_data['frontmatter']['description']}"
                elif 'tags' in file_data['frontmatter']:
                    # Create a simple description from tags
                    tags = file_data['frontmatter']['tags']
                    if isinstance(tags, list) and tags:
                        description = f" - {', '.join(tags[:3])}"  # Show first 3 tags
                
                archive_content += f"- [{title}]({path}){description}\n"
            
            archive_content += "\n"
    
    # Add files without dates
    if no_date_files:
        archive_content += "## Undated Content\n\n"
        for file_data in no_date_files:
            if file_data['filename'] not in ['2099-12-23-Template.md']:  # Skip template
                title = file_data['title']
                path = file_data['path']
                description = ""
                if 'description' in file_data['frontmatter']:
                    description = f" - {file_data['frontmatter']['description']}"
                archive_content += f"- [{title}]({path}){description}\n"
    
    # Write the new archive.md
    archive_path = os.path.join(docs_dir, 'archive.md')
    with open(archive_path, 'w', encoding='utf-8') as f:
        f.write(archive_content)
    
    print(f"Archive rebuilt successfully with {len(files_data)} files!")
    print(f"Generated archive at: {archive_path}")

if __name__ == "__main__":
    main()