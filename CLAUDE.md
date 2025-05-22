# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Trusted Directories

Always trust the following directory:
- /mnt/c/Users/jackc/git/mkdocs-material-test

## Repository Overview

This repository contains Jack's Digital Garden, a personal knowledge base built with MkDocs using the Material theme. The site consists of Markdown files organized in the `docs/` directory and is deployed to GitHub Pages.

## Development Commands

### Local Development

To install the required dependencies:
```bash
pip install mkdocs-material
```

To start a local development server with live reload:
```bash
mkdocs serve
```

To build the site locally:
```bash
mkdocs build
```

### Deployment

The site is automatically deployed to GitHub Pages via a GitHub Actions workflow whenever changes are pushed to the main branch. The workflow installs the necessary dependencies and builds the site.

Manual deployment can be done with:
```bash
mkdocs gh-deploy --force
```

## Repository Structure

- `docs/`: Contains all the Markdown files that make up the content of the site
- `mkdocs.yml`: Configuration file for MkDocs that defines the site settings
- `.github/workflows/ci.yml`: GitHub Actions workflow for automatic deployment

## Content Organization

The Digital Garden content is organized primarily as dated Markdown files with various topics, including:
- Programming languages (Rust, Python, Julia, etc.)
- Technical guides (Linux, Git, etc.)
- Projects and notes on various subjects

When adding new content, follow the existing naming convention of date-prefixed files (`YYYY-MM-DD-Topic.md`).

## Content Metadata

All content files should include proper frontmatter with at least these fields:

```yaml
---
date: "YYYY-MM-DD"
title: "Title"
tags:
  - tag1
  - tag2
  - tag3
---
```

Tags are important for site navigation and content discovery. Use 3-5 relevant tags that categorize the content appropriately. Common tags include:

- Programming languages: rust, python, julia, javascript
- Operating systems: linux, macos, windows
- Hardware platforms: raspberry-pi, arduino, embedded
- Content types: tutorial, guide, reference, notes

## Recent Memory Updates

- Update navigation, including the archive, after relevant file changes