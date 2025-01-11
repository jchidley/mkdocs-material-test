---
date: "2024-05-05"
title: "rust-General"
---
<!-- markdownlint-disable MD025 -->
# rust General
<!-- markdownlint-enable MD025 -->

Update From 27/12/24

[just](https://just.systems/man/en/) for all the things that `cargo` doesn't do.
[Parse, don’t validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/), [Designing with types: Making illegal states unrepresentable](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) and [Make illegal states unrepresentable](https://blog.janestreet.com/effective-ml-revisited/)
Deploy WASM/WASI to the cloud [Fermyon Developer Home](https://developer.fermyon.com/)

[Moo-ving Data Efficiently: Exploring the Rust Cow](https://www.thealphadev.com/2024/01/moo-ving-data-efficiently-exploring.html)
[6 things you can do with the Cow 🐄 in Rust 🦀](https://dev.to/kgrech/6-things-you-can-do-with-the-cow-in-rust-4l55)
[Using Cow in Rust for efficient memory utilization](https://blog.logrocket.com/using-cow-rust-efficient-memory-utilization/)

[You Should Really Know These Traits in Rust](https://www.youtube.com/watch?v=tWa19Td87gw)

## Update 12/8/24

[Plotters is a drawing library aimed to expedite the production of high-quality data visualization in Rust.](https://plotters-rs.github.io/book/intro/introduction.html)
[DataFusion is a very fast, extensible query engine for building high-quality data-centric systems in Rust, using the Apache Arrow in-memory format. DataFusion originated as part of the Apache Arrow project.](https://datafusion.apache.org/user-guide/introduction.html) and [DataFusion is an extensible query engine written in Rust ](https://docs.rs/datafusion/latest/datafusion/index.html)
[DataFusion Examples](https://github.com/apache/datafusion/tree/main/datafusion-examples)
[Effective Rust](https://www.lurklurk.org/effective-rust/title-page.html)
[The Cargo Book](https://doc.rust-lang.org/cargo/reference/overriding-dependencies.html)

### NewType

Newtype provides type safety and encapsulation through the use of a "tuple struct" with a single field.

The data needs to be accessed either by indexing the tuple (i.e. `self.0`) or destructuring. See *Rust By Example's* [New Type Idiom](https://doc.rust-lang.org/rust-by-example/generics/new_types.html), repeated below.  

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Tuple
    let Years(years_as_primitive_2) = years; // Destructuring
}
```

See [Tuple and tuple indexing expressions](https://doc.rust-lang.org/reference/expressions/tuple-expr.html#tuple-and-tuple-indexing-expressions) for tuple indexing. 

[The Newtype Pattern in Rust](https://www.worthe-it.co.za/blog/2020-10-31-newtype-pattern-in-rust.html)
Derive a bunch of traits on your own types, avoiding boilerplate code with [derive_more](https://crates.io/crates/derive_more)
From *Rust Design Patterns'* [Newtype](https://rust-unofficial.github.io/patterns/patterns/behavioural/newtype.html) and also from *Rust By Example's* [New Type Idiom](https://doc.rust-lang.org/rust-by-example/generics/new_types.html#new-type-idiom)

See also: 

* [Using the Newtype Pattern to Implement External Traits on External Types](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#using-the-newtype-pattern-to-implement-external-traits-on-external-types) 
* [Using Tuple Structs Without Named Fields to Create Different Types](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-tuple-structs-without-named-fields-to-create-different-types)
* [Using the Newtype Pattern for Type Safety and Abstraction](https://doc.rust-lang.org/book/ch19-04-advanced-types.html#using-the-newtype-pattern-for-type-safety-and-abstraction)

"If we wanted the new type to have every method the inner type has, implementing the Deref trait (discussed in Chapter 15 in the [Treating Smart Pointers Like Regular References with the Deref Trait](https://doc.rust-lang.org/book/ch15-02-deref.html#treating-smart-pointers-like-regular-references-with-the-deref-trait) section) on the Wrapper to return the inner type would be a solution." from [Using the Newtype Pattern to Implement External Traits on External Types](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#using-the-newtype-pattern-to-implement-external-traits-on-external-types)

But [Is it considered a bad practice to implement Deref for newtypes?](https://stackoverflow.com/questions/45086595/is-it-considered-a-bad-practice-to-implement-deref-for-newtypes) because everything of the underlying type will be visible. Perhaps not what you want. The answer has examples of good, bad and alternative implementation of traits of underlying types. See also "Misuse the Deref trait to emulate inheritance between structs, and thus reuse methods" [Deref polymorphism](https://rust-unofficial.github.io/patterns/anti_patterns/deref.html)

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

[egui - Rust - building a UI to plot a sensor value in real time](https://www.youtube.com/watch?v=zUvHkkkrmIY)
[egui (pronounced "e-gooey") is a simple, fast, and highly portable immediate mode GUI (IMGUI) library for Rust.](https://github.com/emilk/egui)
[The IMGUI paradigm](https://github.com/ocornut/imgui/wiki/About-the-IMGUI-paradigm)
[Short video on IMGUI](https://www.youtube.com/watch?v=LSRJ1jZq90k)
[15 Slide Presentation IMGUI](https://www.cse.chalmers.se/edu/year/2011/course/TDA361/Advanced%20Computer%20Graphics/IMGUI.pdf)
[Rusty_Art ](https://github.com/altunenes/rusty_art) based on [nannou](https://guide.nannou.cc/welcome) that uses egui. Via TimClicks' [Pixelate an image in less than 50 lines of code - Learning Rust Creatively](https://www.youtube.com/watch?v=t4DmszQfD-Q)
[Building a GUI for my Tiling Window Manager in Pure Rust with egui and eframe | Part 1](https://www.youtube.com/watch?v=zZKjBMt4kZ4)
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
