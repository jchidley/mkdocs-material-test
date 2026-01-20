---
date: "2026-01-20"
title: "Documentation Review - Diátaxis Analysis"
tags:
  - documentation
  - review
  - diataxis
  - meta
llm_assisted: true
---
<!-- markdownlint-disable MD025 -->
# Documentation Review - Diátaxis Analysis
<!-- markdownlint-enable MD025 -->

## Introduction

This document reviews all documents in Jack's Digital Garden using the Diátaxis framework. The framework classifies documentation into four types:

| Type | Purpose | User Mode |
|------|---------|-----------|
| **Tutorial** | Learning-oriented | Study |
| **How-to** | Task-oriented | Work |
| **Reference** | Information-oriented | Work |
| **Explanation** | Understanding-oriented | Study |

**Key principle**: Documents should serve *one* purpose—mixing types weakens effectiveness.

## Status Legend

- ✅ Well-structured for its purpose
- ⚠️ Mixed types—needs separation
- 🔄 Link dump—needs restructuring
- 📝 Stub/minimal—needs expansion

---

## Checklist Summary

### Root `/docs/` Directory

| # | Document | Type Assessment | Status |
|---|----------|----------------|--------|
| 1 | `2023-03-21-Julia.md` | ⚠️ Mixed | Reference + Tutorial + Links |
| 2 | `2023-04-08-Julia-Drawing.md` | 🔄 Link dump | Needs content |
| 3 | `2023-04-14-Neovim-Lua.md` | ⚠️ Mixed | How-to + Explanation + Reference |
| 4 | `2023-05-01-VFD-3-Phase-Converter.md` | 🔄 Link dump | Reference + Links |
| 5 | `2023-09-04-Writing-A-Programming-Language.md` | 🔄 Link dump | Reference links only |
| 6 | `2023-09-09-Picocomputer.md` | ⚠️ Mixed | Tutorial fragments + How-to |
| 7 | `2023-11-05-Pi-Pico.md` | 🔄 Link dump | Reference + Links |
| 8 | `2023-11-15-Home-Assistant-ESPHome.md` | 🔄 Link dump | Reference links |
| 9 | `2024-01-17-Microsoft-Surface-Laptop-4.md` | ⚠️ Mixed | How-to + Reference |
| 10 | `2024-01-28-Git.md` | ⚠️ Mixed | How-to + Reference |
| 11 | `2024-02-12-chezmoi.md` | ✅ How-to | Good structure |
| 12 | `2024-02-13-Helix.md` | ⚠️ Mixed | How-to + Reference |
| 13 | `2024-02-29-NixOS.md` | 🔄 Link dump | Needs content |
| 14 | `2024-03-10-How-I-Learned-Rust.md` | ✅ Explanation | Good narrative |
| 15 | `2024-03-17-Asbestos-Roof-Replacement.md` | ⚠️ Mixed | Reference + How-to links |
| 16 | `2024-03-24-House-Electrics.md` | 🔄 Link dump | Massive link collection |
| 17 | `2024-04-14-Plumbing.md` | 🔄 Link dump | Massive link collection |
| 18 | `2024-05-05-Rust-Data.md` | 🔄 Link dump | Reference links |
| 19 | `2024-05-05-Rust-Embedded.md` | ⚠️ Mixed | Reference + How-to + Explanation |
| 20 | `2024-05-05-Rust-General.md` | ⚠️ Mixed | Reference + Explanation |
| 21 | `2024-06-15-Open-Energy-Monitor-Emon.md` | ⚠️ Mixed | How-to + Reference |
| 22 | `2024-08-04-Lathe-Milling.md` | 🔄 Link dump | Reference links |
| 23 | `2024-08-17-Phase-Locked-Loop-PLL.md` | 🔄 Link dump | Reference links |
| 24 | `2024-08-25-Arduino.md` | ⚠️ Mixed | Tutorial fragment + Reference |
| 25 | `2024-08-26-LCD-1602-Pushbutton.md` | ⚠️ Mixed | Reference + Links |
| 26 | `2024-09-15-FreeCAD.md` | 🔄 Link dump | Reference links |
| 27 | `2025-01-23-Miscellaneous-Links.md` | ✅ Reference | Appropriately organized links |
| 28 | `2025-01-23-Python-General-Resources.md` | ✅ Reference | Well-categorized links |
| 29 | `2025-02-08-AI-Coding.md` | ⚠️ Mixed | Reference + Explanation |
| 30 | `2025-02-23-Database_GraphQL.md` | ⚠️ Mixed | How-to + Reference |
| 31 | `2025-03-01-Testing.md` | 📝 Stub | Good structure, needs content |
| 32 | `2025-03-27-DaVinci-Resolve.md` | 📝 Stub | Minimal content |
| 33 | `2025-04-21-Web-Site-Information-and-Manipulation.md` | 📝 Stub | Brief commands only |
| 34 | `2025-05-22-Claude.md` | 📝 Stub | Minimal placeholder |
| 35 | `2026-01-20-Pragmatic-AI-Programming-Blogs.md` | ✅ Reference | Excellent curated list |

---

## Detailed Reviews

### 1. `2023-03-21-Julia.md` ⚠️

**Current state**: Mix of quick start tutorial, reference, workflow guide, and link dump.

**Recommendations**:

- **Split into separate documents**:
  - `Julia-Quick-Start.md` — Tutorial: first program, REPL basics
  - `Julia-Workflow.md` — How-to: package creation, testing workflow
  - `Julia-Reference.md` — Reference: commands, libraries, tools
- **Remove**: Explanation paragraphs from tutorial sections
- **Fix**: The Quick Start has shell code but no expected output—add it

---

### 2. `2023-04-08-Julia-Drawing.md` 🔄

**Current state**: Brief intro + link collection with typos ("Smsh")

**Recommendations**:

- **Either**: Expand with actual usage examples (make it a How-to)
- **Or**: Move links to Julia main page and delete this stub
- **Fix**: Typo "Smsh" → likely "Gmsh" or clarify

---

### 3. `2023-04-14-Neovim-Lua.md` ⚠️

**Current state**: Philosophy/explanation mixed with configuration snippets, installation how-tos, and reference material.

**Recommendations**:

- **Move**: Opening philosophy section to a separate "About Neovim" explanation doc
- **Create**: `Neovim-Setup.md` — How-to guide for setting up on new machines
- **Keep**: Configuration reference sections (Toggleterm, Fugitive, etc.)
- **Add**: Consistent structure to each plugin section (purpose → config → commands)

---

### 4. `2023-05-01-VFD-3-Phase-Converter.md` 🔄

**Current state**: Code snippets and links about Modbus/CRC, no context.

**Recommendations**:

- **Add**: Introduction explaining what this is for
- **Convert to**: Either a Reference (document the protocol) or How-to (connect to VFD)
- **Remove**: Orphaned code snippets without explanation

---

### 5. `2023-09-04-Writing-A-Programming-Language.md` 🔄

**Current state**: Excellent curated link collection but just links.

**Recommendations**:

- **Good as Reference**: Keep the organization
- **Add**: Brief 1-2 sentence descriptions for each link section
- **Consider**: Adding a "Getting Started" section pointing to the best entry point (already has "Additional Reading" but it's buried)

---

### 6. `2023-09-09-Picocomputer.md` ⚠️

**Current state**: Mix of installation instructions and setup guide.

**Recommendations**:

- **Restructure as How-to**: "How to Set Up Picocomputer Development Environment"
- **Add**: Prerequisites section
- **Add**: Expected output after each step
- **Fix**: Incomplete—ends abruptly with empty Links section

---

### 7. `2023-11-05-Pi-Pico.md` 🔄

**Current state**: Well-organized link collection with some setup instructions.

**Recommendations**:

- **Split**: Installation sections → `Pi-Pico-Setup.md` (How-to)
- **Keep**: Link sections as Reference
- **Add**: Brief descriptions for link categories
- **Good**: Has nice info boxes and cross-references

---

### 8. `2023-11-15-Home-Assistant-ESPHome.md` 🔄

**Current state**: Title still says "Template"! Link collection.

**Recommendations**:

- **Fix**: Remove "Template" h1 header—use actual title
- **Structure**: Good categorization, keep as Reference
- **Add**: 1-sentence intro for each section
- **Remove**: Dead links (some are marked as removed already—good!)

---

### 9. `2024-01-17-Microsoft-Surface-Laptop-4.md` ⚠️

**Current state**: Comprehensive but mixes how-to procedures with reference material.

**Recommendations**:

- **Split into**:
  - `WinPE-Recovery-Guide.md` — How-to: Create recovery media
  - `Surface-Drivers.md` — Reference: Driver lists
  - `Windows-Setup.md` — How-to: Application setup workflow
- **Good**: Has working code blocks and clear sections
- **Remove**: Sections about Intune problems (move to troubleshooting)

---

### 10. `2024-01-28-Git.md` ⚠️

**Current state**: How-to mixed with configuration reference.

**Recommendations**:

- **Rename**: More specific title like "Git Setup and Configuration"
- **Good**: Has Related Articles info box
- **Separate**: SSH setup could be its own How-to
- **Add**: Expected output for command examples

---

### 11. `2024-02-12-chezmoi.md` ✅

**Current state**: Clean How-to guide.

**Recommendations**:

- **Good**: Clear steps, minimal
- **Consider**: Adding troubleshooting section
- **Optional**: Add prerequisites (Git installed, etc.)

---

### 12. `2024-02-13-Helix.md` ⚠️

**Current state**: Installation how-to + configuration reference + tips.

**Recommendations**:

- **Split**:
  - Keep installation as How-to
  - Configuration → Reference
  - Tips → separate tips document
- **Good**: Platform-specific sections (Linux, Windows)

---

### 13. `2024-02-29-NixOS.md` 🔄

**Current state**: Just links, no content.

**Recommendations**:

- **Either**: Expand with actual NixOS setup experience
- **Or**: Archive/delete if not being used
- **Add**: At minimum, intro paragraph explaining why these links

---

### 14. `2024-03-10-How-I-Learned-Rust.md` ✅

**Current state**: Personal narrative/explanation of learning journey.

**Recommendations**:

- **Good**: Clear Explanation format
- **Good**: Has Related Rust Documentation info box
- **Keep**: The personal workflow section is valuable
- **Consider**: More links to the actual resources mentioned

---

### 15. `2024-03-17-Asbestos-Roof-Replacement.md` ⚠️

**Current state**: Reference links + safety info.

**Recommendations**:

- **Restructure as How-to**: "How to Safely Remove Asbestos Roof Sheets"
- **Add**: Step-by-step process (currently just links to HSE)
- **Good**: Safety links are essential

---

### 16. `2024-03-24-House-Electrics.md` 🔄

**Current state**: Massive link dump covering solar, batteries, Tesla, monitoring.

**Recommendations**:

- **Split into multiple documents**:
  - `Solar-PV-Setup.md` — Solar installation
  - `Battery-Storage.md` — Tesla/Fox ESS/DIY batteries
  - `Home-Energy-Monitoring.md` — ESP/CT clamps
  - `Smart-Home-Electrics.md` — Fans, thermostats
- **Add**: Intro explaining your setup/goals
- **Good**: Some sections have personal notes ("Update 12/8/24")

---

### 17. `2024-04-14-Plumbing.md` 🔄

**Current state**: Huge link collection on heat pumps, pipes, insulation.

**Recommendations**:

- **Split into**:
  - `Heat-Pump-Installation.md` — Vaillant-specific setup
  - `Underfloor-Insulation.md` — DIY guide
  - `Pipe-Sizing.md` — Reference for flow/pressure
  - `Hot-Water-Systems.md` — Unvented cylinders
- **Good**: Has detailed settings for Vaillant (valuable!)
- **Move**: Settings from Menu > Installer to dedicated reference

---

### 18. `2024-05-05-Rust-Data.md` 🔄

**Current state**: Categorized link reference.

**Recommendations**:

- **Good**: Clean structure
- **Add**: Example code snippets for key crates
- **Add**: "When to use" guidance (polars vs csv vs arrow)

---

### 19. `2024-05-05-Rust-Embedded.md` ⚠️

**Current state**: Mix of HAL comparison, debugging tips, testing guide, C2Rust.

**Recommendations**:

- **Split**:
  - Keep HAL comparison as Reference
  - Testing section → link to Testing.md (already done!)
  - Debugging → separate How-to
  - C2Rust → separate How-to
- **Good**: Excellent info boxes and cross-references

---

### 20. `2024-05-05-Rust-General.md` ⚠️

**Current state**: Large document with learning resources, error handling deep-dive, Unicode handling, etc.

**Recommendations**:

- **This is too long** — Split:
  - `Rust-Error-Handling.md` — Explanation of error handling patterns
  - `Rust-Performance.md` — Benchmarking/NewType/optimization
  - `Rust-Unicode.md` — String/char handling reference
  - Keep tools and learning links as reference
- **Good**: Error handling section is excellent—keep depth

---

### 21. `2024-06-15-Open-Energy-Monitor-Emon.md` ⚠️

**Current state**: Backup procedure + data input reference + firmware.

**Recommendations**:

- **Split**:
  - `Emon-Backup.md` — How-to with working script
  - `Emon-Configuration.md` — Reference for data input
- **Good**: Has working PowerShell example
- **Add**: Expected output for backup script

---

### 22. `2024-08-04-Lathe-Milling.md` 🔄

**Current state**: Reference links for lathe work.

**Recommendations**:

- **Good**: Well-organized categories (DRO, Electronic Lead Screw, etc.)
- **Add**: Your personal setup/recommendations
- **Consider**: Adding a "My Lathe Setup" section

---

### 23. `2024-08-17-Phase-Locked-Loop-PLL.md` 🔄

**Current state**: Just links, brief intro.

**Recommendations**:

- **Either**: Add explanation of PLL concepts
- **Or**: Merge into a signals/DSP document
- **Add**: Why you're interested in PLLs (context)

---

### 24. `2024-08-25-Arduino.md` ⚠️

**Current state**: Brief CLI reference with some commands.

**Recommendations**:

- **Expand**: Into proper How-to "Getting Started with Arduino CLI"
- **Add**: Full example workflow (compile → upload → test)
- **Good**: Has config file snippet

---

### 25. `2024-08-26-LCD-1602-Pushbutton.md` ⚠️

**Current state**: Hardware reference + driver links.

**Recommendations**:

- **Add**: Wiring diagram or pin table
- **Add**: Example code snippet
- **Good**: Has driver links for multiple platforms

---

### 26. `2024-09-15-FreeCAD.md` 🔄

**Current state**: Tips + video links.

**Recommendations**:

- **Add**: Your workflow/techniques
- **Good**: PDF conversion commands are useful—highlight these
- **Consider**: Separating the inkscape commands into utility doc

---

### 27. `2025-01-23-Miscellaneous-Links.md` ✅

**Current state**: Well-organized link collection across many topics.

**Recommendations**:

- **Good**: Appropriate for a "catch-all" reference
- **Good**: Categories are clear
- **Maintain**: Regular link checking (some marked dead already)
- **Consider**: If sections grow large, spin off to dedicated docs

---

### 28. `2025-01-23-Python-General-Resources.md` ✅

**Current state**: Clean categorized Python reference.

**Recommendations**:

- **Good**: Clear categories
- **Good**: Links to related docs
- **Add**: Your recommended "start here" for each category

---

### 29. `2025-02-08-AI-Coding.md` ⚠️

**Current state**: Comprehensive but mixes explanation, reference, and guidance.

**Recommendations**:

- **Split**:
  - `AI-Models-Reference.md` — Model comparison links
  - `AI-Coding-Workflow.md` — How-to use AI for coding
  - Keep MCP section as How-to
- **Good**: Excellent YouTube resource list
- **Good**: OpenAI prompting advice section

---

### 30. `2025-02-23-Database_GraphQL.md` ⚠️

**Current state**: PostgreSQL + GraphQL + Docker setup mix.

**Recommendations**:

- **Split**:
  - `PostgreSQL-Docker-Setup.md` — How-to (already has good example)
  - `GraphQL-Rust.md` — Reference
  - `SQLx-Type-Mapping.md` — Reference (the aichat output)
- **Good**: Docker commands are complete and working

---

### 31. `2025-03-01-Testing.md` 📝

**Current state**: Good structure but mostly placeholder sections.

**Recommendations**:

- **Expand**: Each section needs content
- **Good**: Cross-references to language-specific testing
- **Add**: Your testing philosophy/approach

---

### 32. `2025-03-27-DaVinci-Resolve.md` 📝

**Current state**: Minimal—just one video link and settings location.

**Recommendations**:

- **Either**: Expand with your workflow
- **Or**: Archive until you have more content
- **Add**: At minimum, your common operations

---

### 33. `2025-04-21-Web-Site-Information-and-Manipulation.md` 📝

**Current state**: Three tool examples.

**Recommendations**:

- **Expand**: Into proper How-to for web scraping tools
- **Add**: When to use each tool
- **Good**: Command examples are useful—add more

---

### 34. `2025-05-22-Claude.md` 📝

**Current state**: Placeholder with basic links.

**Recommendations**:

- **Either**: Add your Claude usage patterns
- **Or**: Merge into AI-Coding.md
- **Add**: Specific prompts/techniques that work for you

---

### 35. `2026-01-20-Pragmatic-AI-Programming-Blogs.md` ✅

**Current state**: Excellent curated list with tiers and reasoning.

**Recommendations**:

- **Keep**: Format is great
- **Good**: Has maintenance script
- **Good**: Explains why each blogger is included

---

## Global Recommendations

1. **Create a consistent structure**: Each doc should state its type (Tutorial/How-to/Reference/Explanation) at the top

2. **Split large link dumps**: House Electrics, Plumbing, and Rust-General are too large

3. **Add expected output**: Tutorial and How-to sections need visible results after each command

4. **Fix stubs or archive**: Documents with <100 words of real content should be expanded or merged

5. **Leverage the info boxes**: You already use `!!! info` well—expand this to mark cross-references consistently

6. **Title consistency**: Some titles don't match content (e.g., Home-Assistant still says "Template")

---

## Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Well-structured | 6 | 17% |
| ⚠️ Mixed types | 16 | 46% |
| 🔄 Link dump | 9 | 26% |
| 📝 Stub | 4 | 11% |
| **Total** | **35** | 100% |

---

*Review conducted: 2026-01-20*
*Framework: Diátaxis (diataxis.fr)*
