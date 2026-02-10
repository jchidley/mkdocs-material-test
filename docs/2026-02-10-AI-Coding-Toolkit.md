---
date: "2026-02-10"
title: "AI Coding Toolkit"
tags:
  - ai
  - coding
  - tools
  - llm
  - agents
---
<!-- markdownlint-disable MD025 -->
# AI Coding Toolkit
<!-- markdownlint-enable MD025 -->

What I actually use and recommend for AI-assisted coding, as of February 2026. For my journey here, see [One Year with LLM Coding Agents](2026-02-10-One-Year-With-LLM-Coding-Agents.md). For my early 2025 raw notes, see [AI Coding — Early 2025](2025-02-08-AI-Coding.md).

## How LLMs Work

You don't need to train models, but you need to understand what they are to use them well.

- [Deep Dive into LLMs like ChatGPT](https://youtu.be/7xTGNNLPyMI?si=G7DD2K2sPorAV9le) (Andrej Karpathy) — the single best introduction
- [Andrej Karpathy — Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — if you want to go deeper
- [karpathy/micrograd](https://github.com/karpathy/micrograd) — tiny autograd engine and neural net library
- [karpathy/nanochat](https://github.com/karpathy/nanochat) — minimal full-stack ChatGPT training from scratch
- [Language Models For Software Developers in 17 Minutes](https://www.youtube.com/watch?v=tL1zltXuHO8) — quick practical version, with [code](https://github.com/Me163/youtube/tree/main/Transformers)
- [Transformer Neural Net 3D visualizer](https://bbycroft.net/llm) — interactive, builds intuition

### Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — the transformer paper
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — reasoning models
- [InstructGPT](https://arxiv.org/abs/2203.02155) — how RLHF works

## Finding LLM-Shaped Problems

The real skill isn't prompt crafting — it's recognising which problems are LLM-shaped. LLMs are shockingly good at some things and shockingly bad at others, and the boundary is jagged and non-intuitive.

- [LLMs as a Lossy Encyclopedia](https://adam.holter.com/llms-as-a-lossy-encyclopedia-why-specific-technical-tasks-fail-and-how-to-fix-it/) — great mental model: LLMs shine at processing/understanding/adapting information, not precise retrieval
- [AI tools for software engineers, but without the hype — Simon Willison](https://www.youtube.com/watch?v=uRuLgar5XZw)
- [Simon Willison — 2025: The Year in LLMs](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)
- [Simon Willison — How StrongDM's AI team build serious software without even looking at the code](https://simonwillison.net/2026/Feb/7/software-factory/) — non-interactive "software factory" where specs drive agents

For ongoing coverage: [Ethan Mollick](https://www.oneusefulthing.org/) (LLM-shaped problems), [Addy Osmani](https://addyo.substack.com/) (context engineering), [Simon Willison](https://simonwillison.net/) (practical AI tooling). See [Pragmatic Technical Writers](2026-01-20-Pragmatic-Technical-Writers.md) for the full list.

## Context Engineering

The shift from crafting clever prompts to engineering the input environment — giving the model everything it needs to succeed. This is what pi skills, CLAUDE.md files, and structured prompts do. [Addy Osmani's Elevate](https://addyo.substack.com/) has the best ongoing coverage.

## Understanding Agent Architecture

Agents are simpler than the hype suggests: a loop where an LLM reads inputs, calls tools, and acts on the results. You don't need to build agents from scratch — just understand the loop well enough to use agent tools effectively.

- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — canonical reference. Also: [walkthrough video](https://www.youtube.com/watch?v=bZzyPscbtI8)
- [AI Agents from First Principles](https://cameronrwolfe.substack.com/p/ai-agents) (Cameron R. Wolfe) — builds from basic LLM concepts to agents. Always free.
- [Building Robust Agentic AI](https://tonywood.co/blog/building-robust-agentic-ai-why-simplicity-and-observability-matter-more-than-cleverness) — simple loops with good feedback beat clever architectures
- [Hugging Face — AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) — free, certified

## Tools I Use

### Coding Agents

- [pi](https://github.com/badlogic/pi-mono/releases) — minimal coding agent harness with skills and extensions. What I use daily.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's terminal agent. [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks).
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Google's open-source terminal agent.
- [Codex CLI](https://github.com/openai/codex) — OpenAI's open-source terminal agent.

### Local LLMs

- [LM Studio](https://lmstudio.ai/) — GUI for local models
- [Ollama](https://ollama.com/) — CLI for local models

### Other Tools

- [Gitingest](https://gitingest.com/) — convert Git repos into prompt-friendly text
- [Datasette](https://datasette.io/) / [LLM CLI](https://llm.datasette.io/en/stable/index.html) — Simon Willison's tools for data exploration and LLM interaction
- [Crawl4AI](https://docs.crawl4ai.com/) — open-source LLM-friendly web crawler

## Benchmarks & Model Comparison

- [Arena](https://arena.ai/leaderboard/) — live model comparison, crowdsourced blind votes
- [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models) — intelligence, speed, and price
- [METR](https://metr.org/) — measuring AI on real-world tasks

## Essential Watching

- [Chess tools built with Claude](https://www.youtube.com/watch?v=GSj69yLmwMg) — 61-year-old non-programmer builds real tools through conversational coding
- ["Enhancing LLM Powered Development with Clojure's REPL" — Colin Fleming](https://www.youtube.com/watch?v=oNhqqiKuUmw)
- [3blue1brown](https://www.youtube.com/@3blue1brown) — visual math/ML explanations

## Podcasts

- [Practical AI](https://practicalai.fm/) — accessible, real use cases
- [Latent Space](https://www.latent.space/podcast) — deep AI engineering interviews
- [No Priors](https://www.nopriors.ai/) — builder/founder interviews, no hype

## See Also

- [One Year with LLM Coding Agents](2026-02-10-One-Year-With-LLM-Coding-Agents.md) — my retrospective
- [Pragmatic Technical Writers](2026-01-20-Pragmatic-Technical-Writers.md) — curated list of no-hype bloggers
- [AI Coding — Early 2025](2025-02-08-AI-Coding.md) — where I started
