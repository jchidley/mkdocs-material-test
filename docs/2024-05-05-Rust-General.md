---
date: "2024-05-05"
title: "rust-General"
---
<!-- markdownlint-disable MD025 -->
# rust General
<!-- markdownlint-enable MD025 -->

## Update 12/8/24

[Plotters is a drawing library aimed to expedite the production of high-quality data visualization in Rust.](https://plotters-rs.github.io/book/intro/introduction.html)
[DataFusion is a very fast, extensible query engine for building high-quality data-centric systems in Rust, using the Apache Arrow in-memory format. DataFusion originated as part of the Apache Arrow project.](https://datafusion.apache.org/user-guide/introduction.html) and [DataFusion is an extensible query engine written in Rust ](https://docs.rs/datafusion/latest/datafusion/index.html)
[DataFusion Examples](https://github.com/apache/datafusion/tree/main/datafusion-examples)
[Effective Rust](https://www.lurklurk.org/effective-rust/title-page.html)
[The Cargo Book](https://doc.rust-lang.org/cargo/reference/overriding-dependencies.html)

## Rust based System Tools

[ripgrep is a line-oriented search tool](https://github.com/BurntSushi/ripgrep)
[diff - A syntax-highlighting pager for git, diff, grep, and blame output](https://github.com/dandavison/delta)
[fd is a program to find entries in your filesystem. ](https://github.com/sharkdp/fd)
[bat - A cat(1) clone with wings.](https://github.com/sharkdp/bat)

## Introduction

* currently [This Week in Rust](https://this-week-in-rust.org/blog/2014/06/14/this-week-in-rust-52/)
[The Rustacean Station Podcast](https://rustacean-station.org/)
[idiomatic-rust](https://github.com/mre/idiomatic-rust)
[Idiomatic Rust: Resources And Learning Material](https://corrode.dev/idiomatic-rust/)

[Dioxus is a Rust library for building apps that run on ...](https://dioxuslabs.com/)

[rocket = A web framework for Rust](https://rocket.rs/)

[Tokio is an asynchronous runtime for the Rust](https://tokio.rs/)

[Pretty State Machine Patterns in Rust](https://hoverbear.org/blog/rust-state-machine-pattern/)

[Fornjot is an early-stage CAD kernel, using boundary representation (b-rep), written in the Rust programming language.](https://www.fornjot.app/)

## GUI, TUI, Command Line

[egui (pronounced "e-gooey") is a simple, fast, and highly portable immediate mode GUI library for Rust.](https://github.com/emilk/egui)
[Building cross-platform GUI apps in Rust using egui](https://blog.logrocket.com/building-cross-platform-gui-apps-rust-using-egui/)
[Ratatui is a Rust library for cooking up delicious text user interfaces](https://ratatui.rs/introduction/)
[Awesome Ratatui](https://github.com/ratatui-org/awesome-ratatui)
[Command Line Argument Parser for Rust](https://docs.rs/clap/latest/clap/) see also (Command Line Applications in Rust)[https://rust-cli.github.io/book/index.html]

## Data

(Influx)[https://pimylifeup.com/raspberry-pi-influxdb/]
(Monitoring Your Raspberry Pi System using InfluxDB Telegraf)[https://randomnerdtutorials.com/monitor-raspberry-pi-influxdb-telegraf/]
(MQTT Producer Output Plugin)[https://github.com/influxdata/telegraf/blob/release-1.32/plugins/outputs/mqtt/README.md]
(Flight, DataFusion, Arrow, and Parquet: Using the FDAP Architecture to build InfluxDB 3.0)[https://www.influxdata.com/blog/flight-datafusion-arrow-parquet-fdap-architecture-influxdb/]
(ZigBee@Linux: Getting Data from ZigBee Devices via MQTT to InfluxDB and Grafana)[https://dietrichschroff.blogspot.com/2020/11/zigbeelinux-getting-data-from-zigbee.html]

## Parsers

[pest is a library for writing plain-text parsers in Rust.](https://pest.rs/book/intro.html)
[combine
Fast parser combinators on arbitrary streams with zero-copy support](https://lib.rs/crates/combine)
[Logos is a fast and easy to use lexer generator written in Rust. ](https://logos.maciej.codes/)
[LALRPOP is a parser generator](https://lalrpop.github.io/lalrpop/index.html)
[Welcome to Nominomicon; a guide to using the Nom parser for great good.](https://tfpk.github.io/nominomicon/introduction.html)
[Nom Tutorial](https://github.com/benkay86/nom-tutorial)
[Parsing Text with Nom](https://blog.adamchalmers.com/nom-chars/)

## Concurrency
[tools for concurrent programming](https://github.com/crossbeam-rs/crossbeam)
[Rayon: data parallelism in Rust](https://smallcultfollowing.com/babysteps/blog/2015/12/18/rayon-data-parallelism-in-rust/)

[Grid Search on Large Language Models using Ollama and Rust](https://dezoito.github.io/2023/12/27/rust-ollama-grid-search.html)

### Unicode

use ripgrep to search a downloaded copy of the [Unicode Character Database](https://www.unicode.org/ucd/), the [latest was 16](https://www.unicode.org/versions/Unicode16.0.0/) at the time of writing. There's a zip file of the complete database [UCD.zip](https://www.unicode.org/Public/UCD/latest/ucd/) or an XML version [ucd.all.flat.zip](https://www.unicode.org/Public/UCD/latest/ucdxml/) that shoudl be extracted to use [ripgrep](https://github.com/BurntSushi/ripgrep) on.

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->
