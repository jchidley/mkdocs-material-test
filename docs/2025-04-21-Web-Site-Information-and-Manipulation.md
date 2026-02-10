---
date: "2025-04-21"
title: "Web Site Information and Manipulation"
tags:
  - web
  - tools
  - markdown
  - url-extraction
  - web-scraping
llm_assisted: true
---
<!-- markdownlint-disable MD025 -->
# Web Site Information and Manipulation
<!-- markdownlint-enable MD025 -->

# Introduction

* md-url-extractor .\2023-03-16-Links-iPad.md [tonydub/md-url-extractor: A tool for extracting, cleaning, and exporting URLs from Markdown files.](https://github.com/tonydub/md-url-extractor) — md-url-extractor is a Rust CLI tool that extracts URLs from Markdown files, cleans them by removing tracking parameters and normalizing YouTube lin...
* echo "https://jchidley.github.io" | twars-url2md --stdin  --verbose [twardoch/twars-url2md: Rust tool to fetch multiple URLs and save them into Markdown files](https://github.com/twardoch/twars-url2md) — twars-url2md is a Rust command-line tool that fetches multiple URLs concurrently and converts them to Markdown files, available on crates.io with M...
* monolith https://jchidley.github.io/blog -o %title%.%timestamp%.html [Y2Z/monolith: ⬛️ CLI tool and library for saving complete web pages as a single HTML file](https://github.com/y2z/monolith)

## Web Scraping

[Web scraping](https://en.wikipedia.org/wiki/Web_scraping) — extracting data from websites, typically via automated bots or crawlers.

For LLM use, it's best to convert sites to markdown. As of early 2025 [Crawl4AI](https://crawl4ai.com/mkdocs/) seems to be the most used open-source tool.

- [Subscription Plans | Supadata](https://supadata.ai/pricing) — for web and YouTube transcript extraction.
- [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) — tells crawlers which URLs they can access. Not a security mechanism.
- [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) — XML sitemap format for helping crawlers discover pages.
- [What are Sitemaps](https://www.sitemaps.org/) — overview of the Sitemap protocol.
