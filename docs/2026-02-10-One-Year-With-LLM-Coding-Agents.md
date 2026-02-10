---
date: "2026-02-10"
title: "One Year with LLM Coding Agents"
tags:
  - ai
  - coding
  - tools
  - llm
  - agents
  - claude
  - pi
---
<!-- markdownlint-disable MD025 -->
# One Year with LLM Coding Agents
<!-- markdownlint-enable MD025 -->

## Introduction

On 19th February 2025, I had 10 browser tabs open. They were all about PostgreSQL and SQLite — basic SELECT statements, Rust SQLx tutorials, and a single [Google AI Studio](https://aistudio.google.com/) session where I'd tried to convert markdown to HTML. That was my entire LLM footprint.

A year later I have 41 projects built with AI assistance, 6,352 agent sessions across three different coding agents, and 19 custom AI skills. I thought it would be useful to look at the actual evidence — session logs, browser history, git commits — and see how I got from there to here.

I was watching [Andrej Karpathy](https://karpathy.ai/)'s [Zero to Hero](https://karpathy.ai/zero-to-hero.html) series, reading about RAG with [Qdrant](https://qdrant.tech/), and trying to understand what the [Model Context Protocol](https://modelcontextprotocol.io/introduction) was. I had tabs open for [OpenRouter](https://openrouter.ai/), [Crawl4AI](https://crawl4ai.com/mkdocs/), and [LangChain](https://langchain-ai.github.io/langgraph/). I was doing what I always do with new technology: surveying the landscape before committing.

## The Timeline

### Feb–Apr 2025: Tutorials and First Projects

My first real project was a Monte Carlo retirement simulation in Rust, started 1st March 2025. The commit history starts with "Inital commit" (typo preserved) then 14 commits over three days — tax calculations, survival probability curves, property-based tests. The code worked but the process was entirely chatbot-era: ask a question, read the answer, copy code, paste it, run it, go back.

Around the same time I started building custom [Alpine Linux images for WSL](https://docs.alpinelinux.org/user-handbook/0.1a/Installing/manual.html). Plain commit messages, no conventions, no structured documentation.

### May–Sep 2025: Building Tools Instead of Asking Questions

By May I'd accumulated enough Claude settings to back them up (the file `claude_backup_20250524` still exists). The projects got more ambitious:

- **project-context-manager** — a tool to maintain mental state across concurrent projects, because I was juggling too many to keep track
- **joint_finances** — bank transaction categoriser, 50K+ tx/sec, multiple bank formats, 1,800+ human-verified test transactions. 87% accuracy (target was 99%, I'd be lying if I said I got there)
- **translation** — multi-language document translation using [Azure Translator API](https://azure.microsoft.com/en-gb/products/ai-services/ai-translator/). Processed 200K+ characters

The translation project taught me the most important lesson. I tried to get Claude to translate an entire Japanese compiler textbook ([低レイヤを知りたい人のためのCコンパイラ作成入門](https://www.sigbus.info/compilerbook)). Too big. So I asked it to *build tools* instead. That worked. The insight: **don't ask AI to do big tasks — ask AI to build tools that do big tasks.**

I also tried [aider](https://aider.chat/) on 18th July. Couldn't get past the API key setup on my first attempt. The `.aider.chat.history.md` preserves me declining OpenRouter, declining the documentation link, and giving up. I got it working later.

### Sep–Dec 2025: Hardware and Compilers

Two big projects dominated this period:

**The C compiler.** Building a C compiler step by step in Rust, based on [chibicc](https://github.com/rui314/chibicc)'s 316-commit progression. Rust frontend, LLVM IR backend, containerised in Alpine. Got to step 305 (linker flags). 355,000 lines of code across the repo. Multi-branch workflow with different AI implementations (`claude`, `codex`, `gemini` branches).

**The exercise bike.** Reverse engineering a Life Fitness A080-92218-D000 controller board. This involved physically tracing PCB connections, ordering components (LM393 comparators, TIP Darlington transistors from eBay), writing [QSPICE](https://www.qorvo.com/design-hub/design-tools/interactive/qspice) netlists, and building a Raspberry Pi Pico replacement controller. The session logs from 15th December capture me pasting `mpremote` output in real time, the Pico crashing, and me telling the agent "do better with the mpremote instructions. Stop guessing." That was a turning point — I'd learned that agents can actually verify things and started demanding it.

### Dec 2025–Feb 2026: The Agent Era

December 2025 was when it changed. I started using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (1,235 prompts that month) and [pi](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) (the coding agent I'm using right now). In January 2026, pi logged 4,928 sessions.

What does 5,000 sessions in a month look like? Mostly batch automation:

- 2,329 sessions on the compiler — scripted with `pi --provider anthropic --model claude-sonnet-4-5 -p @prompt/BATCH_STEP.md`
- 1,644 sessions processing browser history into a [mkdocs](https://www.mkdocs.org/) knowledge base
- 69 sessions building [helix-pi](https://github.com/jchidley/helix-pi) — AI agent integration for the [Helix editor](https://helix-editor.com/) via [Steel](https://github.com/mattwparas/steel) (Scheme) plugins
- 22 sessions building an [Octopus Energy](https://octopus.energy/) usage dashboard

## What I Built

Roughly chronological, all with LLM assistance:

| Period | Project | Notes |
|--------|---------|-------|
| Feb 2025 | WSL Alpine Build | Modular Alpine images for WSL |
| Mar 2025 | Monte Carlo Rust | Retirement sim: ONS actuarial data, fat tails, crisis correlation, widowhood effect |
| May 2025 | Project Context Manager | Git-like mental state management |
| Jun 2025 | Translation Toolkit | Azure Translator pipeline: PDF→markdown→translated |
| Jul 2025 | Joint Finances | Bank tx categoriser, multiple formats, regression tested |
| Jul 2025 | MDM Management | PowerShell MDM analysis, 6K lines |
| Jul 2025 | Turing Complete | FPGA dev with [Amaranth HDL](https://amaranth-lang.org/) + IceFUN board |
| Sep 2025 | C Compiler | Rust + LLVM IR, 316 steps, 355K lines |
| Oct 2025 | Ollama Testing | Local LLM benchmarking, Windows + WSL |
| Nov 2025 | Controller Board | Exercise bike reverse engineering, SPICE, Pico replacement |
| Dec 2025 | 19 Agent Skills | QSPICE, pico-firmware, browser-tools, mutation-testing, etc |
| Dec 2025 | SD Card Images | Alpine Pi router images with WiFi AP, DNS/DHCP |
| Dec 2025 | Embassy | Async embedded Rust for ESP32 and Pico |
| Jan 2026 | History Logs | Browser history → mkdocs pipeline |
| Jan 2026 | Helix-Pi | AI agent integration for Helix via Steel |
| Jan 2026 | API Keys (ak) | GPG-encrypted secrets, cross-platform |
| Jan 2026 | Octopus | Energy dashboard with heat pump/degree-day modelling |
| Jan 2026 | UK Energy Monitor | GB electricity generation tracker |
| Feb 2026 | WhatsApp Analysis | Pi extension for iOS WhatsApp SQLite backups |

Languages used: Rust, Python, TypeScript, JavaScript, Shell, PowerShell, Scheme, MicroPython, C, LLVM IR, Amaranth HDL, SPICE netlists. I didn't know most of these a year ago. LLMs make language boundaries surprisingly porous — you only need to understand the concepts.

## What Changed

### How I work now vs then

**Then:** Ask a question in a chat window, copy the answer, paste it, run it, go back. **Now:** Type natural language in a terminal, the agent reads my files, runs tests, edits code, and commits to git. The feedback loop went from minutes to seconds.

**Then:** One tool (ChatGPT or Claude web). **Now:** Claude Code, pi, and factory, with 19 custom skills, structured prompts, and batch pipelines. I tried aider, [Cursor](https://cursor.com/), [Copilot](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/), [Ollama](https://ollama.com/), [Amp](https://ampcode.com/), and [opencode](https://github.com/opencode-ai/opencode). Each taught me something.

**Then:** Accept LLM output on faith. **Now:** Demand verification. I built skills specifically for this — mutation testing, property-based testing, test audits. The exercise bike project taught me this: when the agent guesses instead of checking, tell it to check.

**Then:** Write code. **Now:** Write code *and* infrastructure: agent skills, LLM documentation (CLAUDE.md, AGENTS.md) alongside human documentation, automation patterns, API key managers. Two audiences for every project.

### How the LLMs changed

**Context windows.** Early 2025 models forgot what you told them. By late 2025 I could point an agent at a 355K-line codebase and ask it to implement step 284 of a compiler with awareness of all preceding steps.

**Tool use.** The shift from "LLM generates text" to "LLM reads files, runs commands, edits code, iterates on failures" was the single biggest change. My December exercise bike session — agent reads device output, modifies firmware, updates docs in one flow — wasn't possible a year earlier.

**Batch automation.** Running `pi --provider anthropic --model claude-sonnet-4-5 -p @prompt/BATCH_STEP.md` to process hundreds of compiler steps overnight. Nobody was doing this in February 2025.

**Specialisation.** Generic LLMs are mediocre at everything. An LLM loaded with a 200-line QSPICE skill that knows how to write netlists, parse `.meas` output, and compare against PicoScope data is genuinely useful. That's why I wrote 19 skills.

## What I Learned

The translation project's philosophy document captures it best: don't ask AI to do big tasks, ask AI to build tools that do big tasks.

A year ago I was trying to understand what LLMs were. Now I think of them as a force multiplier for anyone who already knows how to decompose problems, verify outputs, and build systems. 30 years of consulting and architecture experience didn't become irrelevant — they became the scaffolding that makes agent-assisted work productive.

My browser tabs from February 2025 were all tutorials. My tabs from January 2026 include [pi-mono releases](https://github.com/badlogic/pi-mono/releases), [Simon Willison](https://simonwillison.net/), [Peter Steinberger on shipping at inference speed](https://steipete.me/posts/2025/shipping-at-inference-speed), embedded Rust frameworks, and energy dashboards. The tutorials gave way to building. That's the measure.

## See Also

- [AI Coding Toolkit](2026-02-10-AI-Coding-Toolkit.md) — current tools and resources
- [AI Coding — Early 2025](2025-02-08-AI-Coding.md) — my original learning notes
- [Pragmatic Technical Writers](2026-01-20-Pragmatic-Technical-Writers.md) — curated list of no-hype bloggers
- [How I Learned Rust](2024-03-10-How-I-Learned-Rust.md) — the Monte Carlo simulation that started it all
- [Simon Willison: Here's how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
- [Mario Zechner: What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [Peter Steinberger: Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
- [Geoffrey Huntley: Secure codegen patterns](https://ghuntley.com/secure-codegen/)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
