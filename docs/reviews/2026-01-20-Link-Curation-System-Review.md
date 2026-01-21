---
date: "2026-01-20"
title: "Link Curation System Review"
tags:
  - workflow
  - automation
  - links
  - documentation
  - review
llm_assisted: true
---
<!-- markdownlint-disable MD025 -->
# Link Curation System Review
<!-- markdownlint-enable MD025 -->

## Overview

This document analyzes your current link tracking system in `C:\Users\jackc\OneDrive\history_logs` and proposes improvements to reduce friction and automatically suggest links for your Digital Garden.

## Current System

### What You Have

```
C:\Users\jackc\OneDrive\history_logs\
├── open_tabs_*.md           # Browser tab exports (via "List open tabs" extension)
├── downloads/               # Spider-downloaded markdown copies of pages
├── consolidated_open_tabs.* # Aggregated URL data with counts/dates
├── *.py                     # Processing scripts
└── tools/security.md        # API key handling guide
```

### Scripts Inventory

| Script | Purpose | Status |
|--------|---------|--------|
| `extract_urls.py` | Extract URLs from markdown files | ✅ Working |
| `download_urls.py` | Download pages via Spider.cloud → markdown | ✅ Working, but friction |
| `generate_missing_urls.py` | Find URLs not yet downloaded | ✅ Working |
| `consolidate_open_tabs.py` | Aggregate URL counts, dates, excerpts | ✅ Working, **not being used** |
| `md_to_html.py` | Convert markdown → HTML (with encoding detection) | ✅ Useful for previews |
| `convert_to_utf8.py` | Fix file encoding (browser exports non-UTF-8) | ✅ Required for pipeline |
| `compare_lists.py` | Diff two text lists | 🔸 Utility |
| `sort_remove_dups.py` | Dedupe/sort text file | 🔸 Utility |

### Data Flow (Current)

```
Browser tabs → "List open tabs" extension → open_tabs_DD-MM-YYYY, HH-MM-SS.md
                                                    ↓
                                            (manual step - rarely done)
                                                    ↓
                        extract_urls.py → download_urls.py → downloads/
                                                    ↓
                                            (manual step - never done)
                                                    ↓
                        consolidate_open_tabs.py → consolidated_open_tabs.csv
                                                    ↓
                                            (manual step - never done)
                                                    ↓
                                            Digital Garden docs
```

**Problem**: Too many manual steps. The pipeline stops at tab capture.

---

## Issues Identified

### 1. Friction in Spider Downloads

**Current process** (from README):
```bash
# Step 1: Generate missing URLs
uv run generate_missing_urls.py --out-missing missing_urls.txt

# Step 2: Download (requires Bitwarden unlock + FD magic)
7< <(bw get item 'spider.cloud' | jq -r '.fields[] | select(.name=="web_to_md") | .value') \
  uv run download_urls.py missing_urls.txt --out-dir downloads --api-key-fd 7

# Step 3: Update still-missing list
comm -23 <(sort -u missing_urls.txt) <(rg --no-filename -o -P "^Source: \\K.*" downloads | sort -u) > still_missing.txt
```

**Problems**:
- Requires WSL for `<( )` process substitution (Windows native shell can't do this)
- Must have Bitwarden unlocked
- `downloads/` goes to wrong location (WSL path, not OneDrive)
- 3 separate commands to run

### 2. No Link-to-Topic Mapping

The consolidated data has URL counts but no way to know:
- Which URLs belong in which Digital Garden document
- Which URLs are worth curating vs. noise (shopping, auth-gated, etc.)

### 3. Outputs Not Connected

- `consolidated_open_tabs.csv` exists but isn't used
- No bridge to automatically update Digital Garden docs

---

## Proposed Solution

### Goal

**One command** that:
1. Processes recent `open_tabs_*.md` files
2. Identifies frequently-visited URLs (count ≥ 2)
3. Filters out noise (auth-gated, shopping, localhost)
4. Categorizes by topic (maps to Digital Garden docs)
5. Outputs a "review list" of suggested additions
6. Optionally downloads missing pages

### New Script: `suggest_links.py`

A single script that combines consolidation + filtering + categorization:

```python
# suggest_links.py
# Inputs: open_tabs_*.md files
# Outputs: suggested_links.md (for human review)

# Features:
# - Count threshold (default: 2)
# - Domain blocklist (claude.ai/chat, chatgpt.com, localhost, etc.)
# - Topic mapping (github.com/*/embassy* → Rust Embedded, etc.)
# - Outputs markdown with sections per Digital Garden topic
```

### Domain → Topic Mapping (Example)

```yaml
# topic_mapping.yaml
patterns:
  - pattern: "github.com/.*/embassy"
    topic: "Rust Embedded"
    doc: "2024-05-05-Rust-Embedded.md"
  
  - pattern: "docs.rs/"
    topic: "Rust"
    doc: "2024-05-05-Rust-General.md"
  
  - pattern: "embassy.dev"
    topic: "Rust Embedded"
    doc: "2024-05-05-Rust-Embedded.md"
  
  - pattern: "emoncms.org"
    topic: "Energy Monitoring"
    doc: "2024-06-15-Open-Energy-Monitor-Emon.md"
  
  - pattern: "simonwillison.net"
    topic: "AI Coding"
    doc: "2025-02-08-AI-Coding.md"

blocklist:
  - "claude.ai/chat/"
  - "chatgpt.com/"
  - "localhost"
  - "outlook.office.com"
  - "web.whatsapp.com"
  - "amazon.co.uk"
  - "read.amazon.co.uk"
  - "connect.garmin.com"
```

### Simplified Workflow

```
# Daily/weekly: one command
python suggest_links.py

# Output: suggested_links.md
# ├── ## Rust Embedded (3 links)
# │   - [Embassy](https://embassy.dev/) - count: 4, last: 2025-07-19
# │   - [probe-rs](https://probe.rs/...) - count: 2, last: 2025-07-19
# │
# ├── ## AI Coding (5 links)
# │   ...
# │
# └── ## Uncategorized (12 links)
#     - [craftinginterpreters.com](https://...) - count: 4
#     ...

# Human review: 
# - Move good links to appropriate docs
# - Add new patterns to topic_mapping.yaml for uncategorized
# - Ignore/delete the rest
```

### Optional: Spider Integration

Add `--download` flag to also fetch content:

```bash
python suggest_links.py --download
# Runs Spider for URLs that pass the filter
# Saves to OneDrive path (Windows-native)
```

For Windows, simplify the API key handling:

```powershell
# PowerShell profile function
function Invoke-SuggestLinks {
    $env:SPIDER_API_KEY = (bw.exe get password 'spider.cloud')
    python C:\Users\jackc\OneDrive\history_logs\suggest_links.py --download
    Remove-Item Env:SPIDER_API_KEY
}
```

---

## Scripts to Keep vs. Remove

### Keep (Core)

| Script | Reason |
|--------|--------|
| `extract_urls.py` | Useful utility |
| `download_urls.py` | Spider integration |
| `suggest_links.py` | **NEW** - main workflow |
| `topic_mapping.yaml` | **NEW** - configuration |

### Keep (Utilities)

| Script | Reason |
|--------|--------|
| `sort_remove_dups.py` | General utility |
| `compare_lists.py` | Debugging |

### Keep (Encoding Utilities)

| Script | Reason |
|--------|--------|
| `convert_to_utf8.py` | **Required** - browser extension exports non-UTF-8 files (Windows-1252, etc.). Auto-detects encoding via `chardet` and converts to UTF-8. |
| `md_to_html.py` | Useful for quick previews, includes encoding detection. Good for sharing with non-technical people. |

### Consider Removing

| Script | Reason |
|--------|--------|
| `consolidate_open_tabs.py` | Replaced by `suggest_links.py` |
| `generate_missing_urls.py` | Folded into `suggest_links.py` |

### Update README

The current README is comprehensive but documents a workflow you don't use. Replace with simplified instructions for the new single-command workflow.

---

## Implementation Plan

### Phase 1: Create `suggest_links.py`

1. Create `topic_mapping.yaml` with initial patterns based on your docs
2. Write `suggest_links.py` that:
   - Reads `open_tabs_*.md` files with **encoding detection** (via `chardet`) - required because browser extension exports non-UTF-8 files
   - Aggregates counts (like consolidate_open_tabs.py)
   - Filters by blocklist
   - Categorizes by topic patterns
   - Outputs `suggested_links.md`

### Phase 2: Simplify Spider Integration

1. Make `--download` work with Windows-native paths
2. Create PowerShell helper function
3. Update README with simplified workflow

### Phase 3: Connect to Digital Garden

1. Add optional `--update-docs` flag that:
   - Appends new links to appropriate docs (in a "## Recently Added" section)
   - Only for URLs you explicitly approve

---

## Questions and Answers

### Resolved

1. **Count threshold**: 3+ visits (default, configurable via `--min-count N`)

2. **Topic categorization**: Output grouped by topic in `suggested_links.md` for manual review. No auto-insertion into Digital Garden docs - you decide where links go.

3. **Download location**: `C:\Users\jackc\OneDrive\history_logs\downloads\` (current location is correct)

4. **Blocklist approach**: 
   - Default blocklist in `topic_mapping.yaml` (auth-gated, shopping, localhost, etc.)
   - **Refused links file**: `refused_urls.txt` - URLs you've explicitly rejected. Script checks this before suggesting.

5. **Run frequency**: Ad-hoc (on-demand)

### Additional Questions

6. **Refused URLs workflow**: ✅ Both options supported:
   - Manually edit `refused_urls.txt`
   - Run `suggest_links.py --refuse <url>` to add URLs

7. **Count threshold CLI**: ✅ Default of 3, with `--min-count N` to override (e.g., `--min-count 4`)

8. **File tracking**: ✅ Track processed files in `processed_files.txt` (filename + script version)
   - Default: only process new/unprocessed files
   - `--all` to reprocess everything (e.g., after script logic changes)
   - Script `__version__` tracked - bump version to trigger reprocessing of all files
   - All scripts now have `__version__ = "1.0.0"`

---

## Next Steps

1. ~~**Open a new session** with this document as context~~
2. ~~**Answer the questions** above~~ ✅ All questions resolved
3. ~~**Restructure documentation**~~ ✅ Created Diátaxis-structured docs:
   - `README.md` — Signpost with quick start
   - `docs/howto-suggest-links.md` — Main workflow
   - `docs/howto-download-urls.md` — Spider downloads
   - `docs/howto-spider-api-key.md` — API key setup
   - `docs/reference.md` — All scripts documented
   - `docs/explanation.md` — Design decisions and philosophy
4. ~~**Implement** `suggest_links.py` and `topic_mapping.yaml`~~ ✅ Done
5. ~~**Test the workflow** on existing data~~ ✅ Tested:
   - Processed 19 tab export files
   - Found 278 unique URLs
   - Suggested 81 links (3+ visits) across 3 topics
   - Incremental processing works (skips already processed files)
   - `--refuse` flag works
6. ~~**One-time migrations**~~ ✅ Completed 2026-01-20:
   - `downloads_2026-01-20`: 6,834 URLs counted (6,724 new) from Spider downloads
   - `digital_garden_2026-01-20`: 3,030 URLs counted (2,996 new) from Digital Garden docs
   - URLs from migrations are counted but excluded from suggestions (already curated/downloaded)
   - After migrations: 66 links suggested (down from 81 - duplicates excluded)
7. **Iterate** based on what you find useful

---

## Appendix: Sample consolidated_open_tabs.csv Data

Top domains by visit count from your current data:

| Domain | Max Count | Example URLs |
|--------|-----------|--------------|
| `github.com` | 4 | Various repos (embassy, claude-code, etc.) |
| `simonwillison.net` | 4 | AI/coding articles |
| `craftinginterpreters.com` | 4 | Compiler book |
| `docs.anthropic.com` | 3 | Claude docs |
| `emoncms.org` | 3 | Energy monitoring |
| `ghuntley.com` | 3 | AI coding tradecraft |

These would be good candidates for automatic suggestion to your Digital Garden.
