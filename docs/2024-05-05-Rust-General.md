---
date: "2024-05-05"
title: "Rust General"
tags:
  - rust
  - programming
  - performance
  - error-handling
  - unicode
---
<!-- markdownlint-disable MD025 -->
# rust General
<!-- markdownlint-enable MD025 -->

## Additions From 18/1/25

[Crates](https://blessed.rs/crates#section-common-subsection-general) "an unofficial guide to the rust ecosystem"

[RustyLine](https://github.com/kkawakam/rustyline) is a "Readline implementation in Rust that is based on Antirez' Linenoise" see [Similar projects](https://github.com/kkawakam/rustyline?tab=readme-ov-file#similar-projects) for other readline.
[noline](https://github.com/rustne-kretser/noline/tree/master) "is an IO-agnostic #[no_std] line editor providing robust line editing for any system. The core functiunality is IO-free, so it can be adapted to any system be it embedded, async, async embedded, WASM or IPoAC (IP over Avian Carriers)."

As good an argument for rust, from a security point of view, as I've seen
[The existential threat against C++ and where to go from here - Helge Penne - NDC TechTown 2024](https://www.youtube.com/watch?v=gG4BJ23BFBE) along with this one [Moving from C to Rust for embedded software development](https://www.youtube.com/watch?v=YXvebHRn8hs)

[ProjectEuler](https://projecteuler.net/archives), using computer science to explore maths, or vice versa?

Clearly you can go to town on individual math problems, like [Primes | A Software Drag Race](https://github.com/PlummersSoftwareLLC/Primes?tab=readme-ov-file).
[rust Prime Sieve](https://github.com/PlummersSoftwareLLC/Primes/tree/drag-race/PrimeRust), from with Dave's original [Python Prime Sieve](https://github.com/PlummersSoftwareLLC/Primes/blob/original/PrimeSievePY/PrimePY.py)

## Update From 27/12/24

[just](https://just.systems/man/en/) for all the things that `cargo` doesn't do.
Deploy WASM/WASI to the cloud [Fermyon Developer Home](https://developer.fermyon.com/)

## Update 12/8/24

[Plotters is a drawing library aimed to expedite the production of high-quality data visualization in Rust.](https://plotters-rs.github.io/book/intro/introduction.html)
[DataFusion is a very fast, extensible query engine for building high-quality data-centric systems in Rust, using the Apache Arrow in-memory format. DataFusion originated as part of the Apache Arrow project.](https://datafusion.apache.org/user-guide/introduction.html) and [DataFusion is an extensible query engine written in Rust ](https://docs.rs/datafusion/latest/datafusion/index.html)
[DataFusion Examples](https://github.com/apache/datafusion/tree/main/datafusion-examples)

## Packages, Workspaces

Nesting packages, workspaces [How to deal with multiple nested workspace roots?](https://stackoverflow.com/a/77312631/3617057)

start of quote

With a layout like this

```
workspace root
‚îú‚îÄ‚îÄ Cargo.toml (workspace)
‚îú‚îÄ‚îÄ my_app (executable)
|   ‚îî‚îÄ‚îÄ Cargo.toml
‚îú‚îÄ‚îÄ common_lib (lib, via submodule)
|   ‚îî‚îÄ‚îÄ Cargo.toml
‚îî‚îÄ‚îÄ bigger_lib_repo (workspace, via submodule)
    ‚îú‚îÄ‚îÄ Cargo.toml  (workspace)
    ‚îú‚îÄ‚îÄ common_lib (lib, via submodule)
    |   ‚îî‚îÄ‚îÄ Cargo.toml
    ‚îî‚îÄ‚îÄ bigger_lib (lib, not a submodule)
```

With content looking like this

```
# ./Cargo.toml
[workspace]

members = ["app"]

# Important to avoid the multiple workspaces error
exclude = ["bigger_lib_repo"]

# Unsure if this is necessary
resolver = "2"

[patch.crates-io]
# The common dep gets overridden for everybody here
common_lib = { path = "./common_lib" }   
```

```
# ./my_app/Cargo.toml
[package]
name = "my_app"
version = "0.1.0"
edition = "2021"

[dependencies]
# Note this isn't specced using a path
common_lib = { version = "0.1.0" }
bigger_lib = { version = "0.1.0", path = "../bigger_lib_repo/bigger_lib" }
```

```
# ./bigger_lib_repo/Cargo.toml
[workspace]

members = [ "bigger_lib" ]

resolver = "2"

[patch.crates-io]
# Same as the root workspace
common_lib = { path = "./common_lib" }
```

```
# ./bigger_lib_repo/bigger_lib/Cargo.toml
[package]
name = "bigger_lib"
version = "0.1.0"
edition = "2021"

[dependencies]
# Note this isn't specced using a path
common_lib = { version = "0.1.0" }
```

All other Cargo.toml files are not particularly different from what you'd expect.

With this pattern I can

* Build the workspace root without issues
* Build the nested workspace root without issues
* Use publicly exported package members from nested libraries (ie: `bigger_lib::common_lib::MyStruct`)

end of quote

## Learning

use [codewars](https://www.codewars.com/kata/search/rust?q=&xids=completed&beta=false&order_by=total_completed%20desc) select rust as the language, sort by "Most Completed". This is surprisingly useful because the various solutions offer a deeper insight into rust.

[Rust By Practice](https://practice.course.rs/why-exercise.html)

Concise talk on ["Type-Driven API Design in Rust" by Will Crichton](https://www.youtube.com/watch?v=bnnacleqg6k)
Building with types [The Typestate Pattern in Rust](https://cliffle.com/blog/rust-typestate/). Let Get Rusty's video [Improve your Rust APIs with the type state pattern](https://www.youtube.com/watch?v=_ccDqRTx-JU). And No Boilerplate's [Compiler-Driven Development in Rust](https://www.youtube.com/watch?v=Kdpfhj3VM04) video.

[List of Resources to learn Rust - Roadmap From Beginner to Advanced Level](https://github.com/ImplFerris/LearnRust?tab=readme-ov-file)

[A Gentle Introduction To Rust](https://stevedonovan.github.io/rust-gentle-intro/readme.html)

[Teach-rs](https://github.com/trifectatechfoundation/teach-rs) is a university course for computer science students, introducing the Rust Programming Language, and is available for anyone who wants to teach Rust. [Bart Massey: Embedded: Rust Education's Next Big Thing](https://www.youtube.com/watch?v=5avqwnG1h5M)

[Effective Rust](https://www.lurklurk.org/effective-rust/title-page.html)

[Parse, don‚Äôt validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/), [Designing with types: Making illegal states unrepresentable](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) and [Make illegal states unrepresentable](https://blog.janestreet.com/effective-ml-revisited/)

[Moo-ving Data Efficiently: Exploring the Rust Cow](https://www.thealphadev.com/2024/01/moo-ving-data-efficiently-exploring.html)
[6 things you can do with the Cow üêÑ in Rust ü¶Ä](https://dev.to/kgrech/6-things-you-can-do-with-the-cow-in-rust-4l55)
[Using Cow in Rust for efficient memory utilization](https://blog.logrocket.com/using-cow-rust-efficient-memory-utilization/)

[You Should Really Know These Traits in Rust](https://www.youtube.com/watch?v=tWa19Td87gw)

## Error Handling

* For a general introduction to error handling see [the book](https://doc.rust-lang.org/book/ch09-00-error-handling.html), see also the helpful [Rust container cheat sheet](https://docs.google.com/presentation/d/1q-c7UAyrUlM-eZyTo1pd8SZ0qwA_wYxmPZVOQkoDmH4/edit#slide=id.p) for memory layouts. — This is a chapter introduction from The Rust Programming Language book explaining Rust's error handling philosophy, which distinguishes between rec...
* Details about the various `Result` error handling functions, including how to convert to and from various `Result` and `Error` combinations see [Rust Error Handling Cheatsheet - Result handling functions](https://gist.github.com/e-t-u/70f25d4566468adc43a4df43667cedb6) — A comprehensive cheatsheet documenting Rust's 21 Result error handling functions, organized by their behavior on Ok and Err variants, with examples...
* For a detailed look at how Rust does io error handling see [Study of std::io::Error](https://matklad.github.io/2020/10/15/study-of-std-io-error.html), [Error Handling in a Correctness-Critical Rust Project](https://sled.rs/errors.html) and [library/std/src/io/error.rs](https://github.com/rust-lang/rust/blob/master/library/std/src/io/error.rs) with [library/std/src/io/error/repr_unpacked.rs](https://github.com/rust-lang/rust/blob/master/library/std/src/io/error/repr_unpacked.rs) — A detailed technical analysis of Rust's std::io::Error implementation, examining how it balances encapsulation with inspectability through a three-...
* How Jeremy Chone does his [Rust Error Handling - Best Practices](https://www.youtube.com/watch?v=j-VQCYP7wyw) — A tutorial on Rust error handling best practices, distinguishing between loose error handling for test code (using Box<dyn Error>) and strict, stru...

### dyn Error

The `dyn` keyword here is for [Dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch) which "is the process of selecting which implementation of a polymorphic operation (method or function) to call at run time". Normally in rust we're trying to make everything static because it's quick and can be checked at compile time. In the case of errors, especially ones that are not going to be handled by the program itself, the runtime costs seem unimportant to me. [Using Trait Objects That Allow for Values of Different Types](https://doc.rust-lang.org/book/ch17-02-trait-objects.html) and see [Rust Powered Polymorphism ‚ö°Ô∏è With Traits](https://www.youtube.com/watch?v=CHRNj5oubwci)

see [this explanation from Jeremy](https://youtu.be/j-VQCYP7wyw?si=35WmDNFLqlOnjf0p&t=840)

To be able to use the `?` with for your functions requires that the returned error (say `MyOwnError`) `impl std::error::Error for MyOwnError {}`: that requires `Display` is implemented for `MyOwnError` and `Display` requires `Debug`. In practice, it is suggested that you use `Error` within your own module and not a custom name like `MyOwnError`. The function using `?` with your function will probably use `type Result<T> = core::result::Result<T, Box<dyn std::error::Error>>;` and thus itself return `Result<T>`.

In addition, if you're converting errors to simple strings (using `map_err` for example) then you'll need to implement

```rust
impl From<&str> for Error {
    fn from(value: &str) -> Self {
        Self::PassThrough(value.to_string())
    }
}
```

Where `PassThrough(String)` is one of `MyOwnError` enums.

So at compile time, if I don't know the exact type but I do know that the type implements (a) specific trait(s) then I can use dynamic dispatch. Traits are boxed. If I do know the specific type(s) then I can implement generics or enums.

[How to manually return a Result<(), Box<dyn Error>>?](https://stackoverflow.com/a/51550905/3617057)
[Help understanding return for Box<dyn Error>](https://users.rust-lang.org/t/help-understanding-return-for-box-dyn-error/33748)
"For `Box<dyn Error>` (and its variants with `+ Send + Sync`), there are `From<&str>` and `From<String>` implementations to convert strings into errors.
And `v.into()` returns `From::from(v)` by default."
[dyn Trait](https://blog.rust-lang.org/2018/06/21/Rust-1.27.html#dyn-trait)
[Defining a Trait](https://doc.rust-lang.org/stable/book/ch10-02-traits.html)
[Using Trait Objects That Allow for Values of Different Types](https://doc.rust-lang.org/book/ch17-02-trait-objects.html)
[Trait objects](https://doc.rust-lang.org/reference/types/trait-object.html)
[What makes something a "trait object"?](https://stackoverflow.com/questions/27567849/what-makes-something-a-trait-object)
[How do you actually use dynamically sized types in Rust?](https://stackoverflow.com/a/25753422/3617057)
[Trait Objects vs Generics in Rust](https://web.archive.org/web/20240605124806/https://medium.com/@richinex/trait-objects-vs-generics-in-rust-426a9ce22d78)

### Custom Error, static

Green Tea Coding's video guide to [make your custom errors fly!](https://www.youtube.com/watch?v=KrZ0nmpNVOw&t=0). He wrote a nice, broken, [csv program](https://github.com/Thodin/custom-errors/) to illustrate his video .
[How do you define custom `Error` types in Rust?](https://stackoverflow.com/questions/42584368/how-do-you-define-custom-error-types-in-rust)

For a concise example, see how the standard library does a custom error: [std::str::FromStr](https://doc.rust-lang.org/std/str/trait.FromStr.html) along with how to implement a trait :-).
Also [A Simpler Way to See Results](https://www.youtube.com/watch?v=s5S2Ed5T-dc)

Insight into error handling [Nom's error is referencing data owned by the calling function](https://github.com/rust-bakery/nom/issues/1706#issuecomment-2578820853)

How [HASH.dev](https://hash.dev/) people were handing errors and why they wrote a blog describing their problems and [announcing](https://hash.dev/blog/announcing-error-stack) [error-stack](https://docs.rs/error-stack/latest/error_stack/). See also Let's Get Rusty's video: [Simple error handling in Rust](https://www.youtube.com/watch?v=g6WUHcyjsfc)

## Benchmarking and Performance

[The Rust Performance Book](https://nnethercote.github.io/perf-book/benchmarking.html) and a [brief description of benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html).

Memory allocations seems to be a bottleneck and algorithms can have a huge effect. Even allocating memory `with_capacity` can double system performance. Changing allocators definitely helps [How to create a custom memory allocator in Rust](https://www.brochweb.com/blog/post/how-to-create-a-custom-memory-allocator-in-rust/) but while it is less than the algorithm chosen, it measurably improves performance and is almost no effort, see this crate [snmalloc-rs](https://crates.io/crates/snmalloc-rs) for bindings to `snmalloc`.

"changing various container arguments to slices, such as changing &mut Vec<T> arguments to &mut [T]"

For faster linking [mold: A Modern Linker](https://github.com/rui314/mold?tab=readme-ov-file) add this to `~/.cargo/config.toml`:

```
[build]
rustflags = ["-C", "link-arg=-fuse-ld=mold"]
```

or set this environment variable `RUSTFLAGS="-C link-arg=-fuse-ld=mold"`.Potentially `"-C", "target-cpu=native"` can help too.

`let r = o.ok_or_else(|| expensive()); // evaluates `expensive()` only when needed`

"Iterator::collect converts an iterator into a collection such as Vec, which typically requires an allocation. You should avoid calling collect if the collection is then only iterated over again. For this reason, it is often better to return an iterator type like impl Iterator<Item=T> from a function than a Vec<T>."

Are there better ways to do the same thing see [String concatenations benchmarks (updated)](https://www.reddit.com/r/rust/comments/t06hk7/string_concatenations_benchmarks_updated/)

[Catch Performance Regressions in CI](https://bencher.dev/) from bencher.dev which also has a [benchmarking overview](https://bencher.dev/docs/explanation/benchmarking/)

### Some specific benchmarking tools

* [hyperfine](https://github.com/sharkdp/hyperfine) is a command-line benchmarking tool.
* [Criterion.rs](https://bheisler.github.io/criterion.rs/book/criterion_rs.html) is a statistics-driven micro-benchmarking tool. The most used benchmarking tool for rust - a haskell port. First released in 2017, most popular tool. — Criterion.rs is a statistics-driven micro-benchmarking library for Rust, ported from Haskell's Criterion, that automatically detects performance re...
* [Iai-Callgrind](https://github.com/iai-callgrind/iai-callgrind) is a benchmarking framework/harness which uses Valgrind's Callgrind and other Valgrind tools like DHAT, Massif, ... to provide extremely accurate and consistent measurements of Rust code, making it perfectly suited to run in environments like a CI. Iai-Callgrind is integrated in Bencher.
* [Divan](https://nikolaivazquez.com/blog/divan/) is a Rust framework for quick comfy benchmarking. First released in 2023, #2 to Criterion on Lib.rs. — Divan is a Rust benchmarking framework that offers a simpler API than Criterion while providing features like allocation profiling, generic paramet...

For detailed profiling see [My Current Pick of Rust Performance Optimization Tools](https://www.worthe-it.co.za/blog/2021-06-19-rust-performance-optimization-tools.html)

For a good explanation of flame graphs see [Flame Graphs Explained: Illuminate Performance Issues the Quick and Easy Way](https://seeinglogic.com/posts/flame-graphs-explained/), python based but relevant for rust too.

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

* currently [This Week in Rust](https://this-week-in-rust.org/blog/2014/06/14/this-week-in-rust-52/) — This Week in Rust issue 52 covers major breaking changes including the removal of ~[T] syntax and @-syntax (ending 'sigil tyranny'), new RFCs like ...
[The Rustacean Station Podcast](https://rustacean-station.org/)
[idiomatic-rust](https://github.com/mre/idiomatic-rust)
[Idiomatic Rust: Resources And Learning Material](https://corrode.dev/idiomatic-rust/)

[Dioxus is a Rust library for building apps that run on ...](https://dioxuslabs.com/)

[rocket = A web framework for Rust](https://rocket.rs/)

[Tokio is an asynchronous runtime for the Rust](https://tokio.rs/)

[Pretty State Machine Patterns in Rust](https://hoverbear.org/blog/rust-state-machine-pattern/)

[Fornjot is an early-stage CAD kernel, using boundary representation (b-rep), written in the Rust programming language.](https://www.fornjot.app/)

## GUI, TUI, Command Line

[Full Stack Rust with Leptos](https://benw.is/posts/full-stack-rust-with-leptos)
[Using Rust and Leptos to build beautiful, declarative UIs](https://blog.logrocket.com/using-rust-leptos-build-beautiful-declarative-uis/)

[egui - Rust - building a UI to plot a sensor value in real time](https://www.youtube.com/watch?v=zUvHkkkrmIY)
[egui (pronounced "e-gooey") is a simple, fast, and highly portable immediate mode GUI (IMGUI) library for Rust.](https://github.com/emilk/egui)
[The IMGUI paradigm](https://github.com/ocornut/imgui/wiki/About-the-IMGUI-paradigm)
[Short video on IMGUI](https://www.youtube.com/watch?v=LSRJ1jZq90k)
[15 Slide Presentation IMGUI](https://www.cse.chalmers.se/edu/year/2011/course/TDA361/Advanced%20Computer%20Graphics/IMGUI.pdf)
[Rusty_Art ](https://github.com/altunenes/rusty_art) based on [nannou](https://guide.nannou.cc/welcome) that uses egui. Via TimClicks' [Pixelate an image in less than 50 lines of code - Learning Rust Creatively](https://www.youtube.com/watch?v=t4DmszQfD-Q)
[Building a GUI for my Tiling Window Manager in Pure Rust with egui and eframe | Part 1](https://www.youtube.com/watch?v=zZKjBMt4kZ4)
[Building cross-platform GUI apps in Rust using egui](https://blog.logrocket.com/building-cross-platform-gui-apps-rust-using-egui/)
[Ratatui is a Rust library for cooking up delicious text user interfaces](https://ratatui.rs/)
[Awesome Ratatui](https://github.com/ratatui-org/awesome-ratatui)
[Command Line Argument Parser for Rust](https://docs.rs/clap/latest/clap/) see also [Command Line Applications in Rust](https://rust-cli.github.io/book/index.html)

## Data, Containers

[Rust container cheat sheet](https://docs.google.com/presentation/d/1q-c7UAyrUlM-eZyTo1pd8SZ0qwA_wYxmPZVOQkoDmH4/edit#slide=id.p)

[Influx](https://pimylifeup.com/raspberry-pi-influxdb/)
[Monitoring Your Raspberry Pi System using InfluxDB Telegraf](https://randomnerdtutorials.com/monitor-raspberry-pi-influxdb-telegraf/)
[MQTT Producer Output Plugin](https://github.com/influxdata/telegraf/blob/release-1.32/plugins/outputs/mqtt/README.md)
[Flight, DataFusion, Arrow, and Parquet: Using the FDAP Architecture to build InfluxDB 3.0](https://www.influxdata.com/blog/flight-datafusion-arrow-parquet-fdap-architecture-influxdb/)
[ZigBee@Linux: Getting Data from ZigBee Devices via MQTT to InfluxDB and Grafana](https://dietrichschroff.blogspot.com/2020/11/zigbeelinux-getting-data-from-zigbee.html)

## Parsers

A tutorial on [Winnow](https://docs.rs/winnow/latest/winnow/index.html) - [The Winnow Way](https://docs.rs/winnow/latest/winnow/_tutorial/index.html)
[pest is a library for writing plain-text parsers in Rust.](https://pest.rs/book/intro.html)
[combine
Fast parser combinator on arbitrary streams with zero-copy support](https://lib.rs/crates/combine)
[Logos is a fast and easy to use lexer generator written in Rust. ](https://logos.maciej.codes/)
[LALRPOP is a parser generator](https://lalrpop.github.io/lalrpop/index.html)
[Welcome to Nominomicon; a guide to using the Nom parser for great good.](https://tfpk.github.io/nominomicon/introduction.html)
[Nom Tutorial](https://github.com/benkay86/nom-tutorial)
[Parsing Text with Nom](https://blog.adamchalmers.com/nom-chars/)
[Parsing bitstreams with Nom](https://blog.adamchalmers.com/nom-bits/)
[Rust's nom as a streaming parser](https://blog.claude.nl/posts/nom-as-a-streaming-parser/)
[Parsing Text with Nom](https://stevedonovan.github.io/rust-gentle-intro/nom-intro.html)
[Implementing a Text-File Parser with nom](https://amedee.me/post/2019-09-01-tsplib-nom-parser/)
[Parsing in Rust with nom](https://blog.logrocket.com/parsing-in-rust-with-nom/)

## Concurrency
[tools for concurrent programming](https://github.com/crossbeam-rs/crossbeam)
[Rayon: data parallelism in Rust](https://smallcultfollowing.com/babysteps/blog/2015/12/18/rayon-data-parallelism-in-rust/)

[Grid Search on Large Language Models using Ollama and Rust](https://dezoito.github.io/2023/12/27/rust-ollama-grid-search.html)

### Unicode, Strings, str, char, u8

If you're trying to deal with individual characters, at some point a string (or &str) will need to be decoded, iteratively, using either [chars](https://doc.rust-lang.org/std/primitive.str.html#method.chars) or [char_indices](https://doc.rust-lang.org/std/primitive.str.html#method.char_indices). Lots of use of collections and note that the collection of characters is almost certainly going to be larger than the string (4 times larger for an UTF-8 encoded ASCII string).

```rust
#[allow(dead_code)]
fn maskify(cc: &str) -> String {
    let replace = cc.chars().count().saturating_sub(4);
    if replace == 0 {
        cc.to_string()
    } else {
        let (idx, _) = cc.char_indices().nth(replace).unwrap();
        "#".repeat(replace) + &cc[idx..]
    }
}

mod tests {
    use super::maskify;

    #[test]
    fn it_masks_example_strings() {
        assert_eq!(maskify("4556364607935616"), "############5616");
        assert_eq!(maskify("1"), "1");
        assert_eq!(maskify("11111"), "#1111");
    }
}
```

[Why is capitalizing the first letter of a string so convoluted in Rust?](https://stackoverflow.com/questions/38406793/why-is-capitalizing-the-first-letter-of-a-string-so-convoluted-in-rust)

For some examples of how this can handled see the source code of [oh heck, a case conversion library](https://github.com/withoutboats/heck/tree/master) and the archived, and mostly ascii based, [Inflector](https://github.com/whatisinternet/Inflector/tree/master)

Rust uses ut8 encoding for strings, etc, chars are u32 which is the size of [Unicode Scalar Value](https://unicode.org/glossary/#unicode_scalar_value). This isn't the same as a [Code point: Any value in the Unicode codespace.](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G22700). For some languages characters can be made up of several code points. [Unicode¬Æ Standard Annex #29](https://www.unicode.org/reports/tr29/) 

"A single Unicode code point is often, but not always the same as a basic unit of a writing system for a language, or what a typical user might think of as a ‚Äúcharacter‚Äù. There are many cases where such a basic unit is made up of multiple Unicode code points. To avoid ambiguity with the term character as defined for encoding purposes, it can be useful to speak of a user-perceived character. For example, ‚ÄúG‚Äù + grave-accent is a user-perceived character: users think of it as a single character, yet is actually represented by two Unicode code points." [Unicode¬Æ Standard Annex #29](https://www.unicode.org/reports/tr29/) 

Rust is going to try pretty hard to make sure that these are valid conversions. Strings convert to u8 (bytes) in very specific ways. Ways that include variable multi-byte encoding.

[How do I convert between String, &str, Vec\<u8\> and &\[u8\]](https://stackoverflow.com/a/41034751/3617057)

```text
&str    -> String  | String::from(s) or s.to_string() or s.to_owned()
&str    -> &[u8]   | s.as_bytes()
&str    -> Vec<u8> | s.as_bytes().to_vec() or s.as_bytes().to_owned()
String  -> &str    | &s if possible* else s.as_str()
String  -> &[u8]   | s.as_bytes()
String  -> Vec<u8> | s.into_bytes()
&[u8]   -> &str    | s.to_vec() or s.to_owned()
&[u8]   -> String  | std::str::from_utf8(s).unwrap(), but don't**
&[u8]   -> Vec<u8> | String::from_utf8(s).unwrap(), but don't**
Vec<u8> -> &str    | &s if possible* else s.as_slice()
Vec<u8> -> String  | std::str::from_utf8(&s).unwrap(), but don't**
Vec<u8> -> &[u8]   | String::from_utf8(s).unwrap(), but don't**
```

* target should have explicit type (i.e., checker can't infer that)
** handle the error properly instead

[rust converting bytes chars and strings](https://peterlyons.com/problog/2017/12/rust-converting-bytes-chars-and-strings/).

```rust
use std::str;

fn main() {
    // This is "hello world" as an array of bytes.
    // You can also start from a byte string b"hello world" and debug print that to get the
    // utf8 encoded decimal values
    // b"a string" is only valid on ASCII
    println!("hello byte string: {:?}", b"hello world");

    // OK so let's say you have an array of u8s
    let array_of_u8 = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100];

    // [u8] to String (lossy)
    // Any invalid bytes that are not utf8 will be replaced with
    // the unicode replacement character '\u{FFFD}'
    // You get a Cow (Clone on Write) not exactly a String
    let string_utf8_lossy = String::from_utf8_lossy(&array_of_u8);
    println!("string_utf8_lossy: {}", string_utf8_lossy);

    // [u8] to String (result)
    // The non-lossy version needs a vec not an array
    let mut vec_of_u8 = vec![];
    vec_of_u8.extend_from_slice(&array_of_u8);
    let string_utf8_result = String::from_utf8(vec_of_u8).unwrap();
    println!("string_utf8_result: {}", string_utf8_result);

    // [u8] to str (result)
    let str_utf8_result = str::from_utf8(&array_of_u8).unwrap();
    println!("str_utf8_result: {}", str_utf8_result);

    // [u8] to str (lossy)
    // There is no str::from_utf8_lossy. Have to use String::from_utf8_lossy
    // [u8] to Vec<char>
    // only valid for ASCII encodings?
    let vec_of_chars: Vec<char> = array_of_u8.iter().map(|byte| *byte as char).collect();
    println!("vec_of_chars: {:?}", vec_of_chars);

    // Vec<char> to Vec<u8>
    let vec_of_u8s: Vec<u8> = vec_of_chars.iter().map(|c| *c as u8).collect();
    println!("vec_of_u8s: {:?}", vec_of_u8s);

    // Vec<char> to String
    let mut string_of_collected_chars: String = vec_of_chars.iter().collect();
    println!("string_of_collected_chars: {}", string_of_collected_chars);

    // Now we have a mutable String. We can push chars
    string_of_collected_chars.push('!');

    // and we can push a str
    string_of_collected_chars.push_str("!!");

    // String to str
    let str_slice = &string_of_collected_chars[..5];
    println!("str_slice: {}", &str_slice);

    // String to [u8]
    let array_of_u8_from_string = string_of_collected_chars.as_bytes();
    println!("array_of_u8_from_string: {:?}", array_of_u8_from_string);

    // String to Vec<char>
    let vec_of_chars_to_string: Vec<char> = string_of_collected_chars.chars().collect();
    println!("vec_of_chars: {:?}", vec_of_chars_to_string);

    // String from several Strings
    let concat_strings = vec!["abc".to_string(), "def".to_string()].concat();
    println!("concat_strings: {}", concat_strings);
    let joined_strings = vec!["abc".to_string(), "def".to_string()].join("---");
    println!("joined_strings: {}", joined_strings);
}
```

There are also these other functions, and probably more too.
 
```text
std::str::from_utf8_unchecked
std::string::String::from_utf8
String::from_utf8_lossy
```

Unicode support modules for Rust. [unicode-rs](https://unicode-rs.github.io/) this includes [unicode-normalization](https://unicode-rs.github.io/unicode-normalization/unicode_normalization/index.html), [unicode-segmentation](https://unicode-rs.github.io/unicode-segmentation/unicode_segmentation/index.html), [unicode-width](https://unicode-rs.github.io/unicode-width/unicode_width/index.html) and [unicode-xid](https://unicode-rs.github.io/unicode-xid/unicode_xid/index.html)

use ripgrep to search a downloaded copy of the [Unicode Character Database](https://www.unicode.org/ucd/), the [latest was 16](https://www.unicode.org/versions/Unicode16.0.0/) at the time of writing. There's a zip file of the complete database [UCD.zip](https://www.unicode.org/Public/UCD/latest/ucd/) or an XML version [ucd.all.flat.zip](https://www.unicode.org/Public/UCD/latest/ucdxml/) that should be extracted to use [ripgrep](https://github.com/BurntSushi/ripgrep) on.

