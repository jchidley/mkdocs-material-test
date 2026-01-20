---
date: "2024-03-10"
title: "How I Learned Rust"
tags:
  - rust
  - programming
  - learning
---
<!-- markdownlint-disable MD025 -->
# How I Learned Rust
<!-- markdownlint-enable MD025 -->

## Introduction

I found Python to be an incredibly useful language that's available almost everywhere - even on micro-controllers. Its amazing libraries cover a huge range of needs and are performant. I would still be using Python as my go-to langage if I hadn't needed to do a Monte Carlo simulation of my own finances. There didn't appear to be a suitable library to fit my needs and, owing to the compute intensive nature of the problem, I found that I would have to develop a library in another, more performant language. Thus I discovered the "2 language problem" you have a flexible, easy to learn and use language (e.g. Python) but need a highly performant language for it's libraries (e.g. C).

I initially looked using `rust` through the [pyo3](https://github.com/PyO3/pyo3) library but it became obvious that this was no quick fix. So I looked for alternatives and found that [julia](https://julialang.org/) met my needs. I developed my little application and I was happy. However, there are limitations with julia: 1) it is a niche language and doesn't seem like to gain really broad application 2) it requires a runtime and 3) it doesn't easily run on micro-controllers.

So I started looking again. I wanted a langauge with broad applicability, didn't suffer the 2 langague problem, is higly performant, had a welcoming beginner-friendly community and is strongly typed (this goes hand-in-hand with great performance). It seems to be used for a very large, and expanding rapidly, set of computing tasks - gaming, embedded programming, GUI development, web development, operating systems, etc. `rust` comes with a long-to-get-productive learning curve. I don't think that it's espcially difficult to learn.

I also found [mojo](https://www.modular.com/max/mojo) which "combines the usability of Python with the performance of C, unlocking unparalleled programmability". Mojo targets AI but looks like it'll work as a general programming langage. It's in its very early stages so I'm keeping an eye on it.

The clostest thing that I've found to a hands on and, relatively, short tutorial is this one for [command line apps in Rust](https://rust-cli.github.io/book/index.html). It covers a *lot* of ground and has a set of [resources](https://rust-cli.github.io/book/resources/index.html)

* [Learn Rust](https://www.rust-lang.org/learn)
* [rustlings](https://rustlings.cool/)

## Workflow and Setup

My primiary machines are a 16 GB Windows Surface Laptop 3 and an 8GB Raspberry Pi 5. I think these represent excellent value for money. I also use a macbook and Linux desktops. I have been using PCs for over 3 decades and Windows since "386". It's in my muscle memory. There appears to few examples of people programming rust on windows, so that's another reason to use it. 

I use the current versions of [helix editor](https://helix-editor.com/), using [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4) inside the [Windows Terminal](https://github.com/microsoft/terminal). I prefer to use cross-platform `rust`-based command line tools. I use [zoxide](https://github.com/ajeetdsouza/zoxide), [ripgrep](https://github.com/BurntSushi/ripgrep) and [fd](https://github.com/sharkdp/fd) all the time. Feel free to use whatever you're comfortable with.

Install `rust` using `rustup`

```powershell
cd $env:TEMP # Windows temporary directory
cargo new --lib rust_explore # almost all programming involves creating and using libraries
cargo test --lib tests -- --nocapture # `-- --nocapture` for `println!` and friends
Set-ExecutionPolicy Unrestricted -Scope Process; iex (iwr "https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.ps1").Content # binary install for crates
cargo binstall cargo-watch # watcher
# open 3 panes: 1) `hx .\src\lib.rs` editor 2) `cargo watch -x check` hot-loading compile checking 3) `cargo test --lib explore -- --nocapture` or `cargo add some-crate` or some other command
```

I rename the module `tests` to `explore` and use that to explore the rust language as I'm learning it. 

I make sure that the test includes a `let result =` assigment directly before `dgb!{result);`. Once I am compfortable with this, I use the result in an appropriate `assert` macro for the final test.

This closely mimics my ideal development process. First I explore the libraries I might use and then I use tests as I develop the code. Sometimes its code first, sometimes its test first; I write documentation, including examples, at the same time. I aim for 100% coverage of the code with tests and documentation. I'd by lying if I wrote that I always do this.

Given that almost everyting that I do involves the command line I used [Command line apps in Rust](https://rust-cli.github.io/book/index.html) book as a reference implemetation and tutorial.

## Getting Started

I did a skim read of the [The Rust Programming Language](https://doc.rust-lang.org/stable/book/title-page.html), and watched [doggo dot rs](https://web.archive.org/web/2024/https://www.youtube.com/@doggodotrs)'s full rust course *(channel archived)*.

I followed this up with working my way through [rustlings](https://github.com/rust-lang/rustlings), Trevor Sullivan's [Rust Programming Tutorial](https://youtube.com/playlist?list=PLDbRgZ0OOEpUkWDGqp91ODn0dk7LPBAUL) and *Mastering Rust - Second Edition*
by *Rahul Sharma and Vesa Kaihlavirta* concurrently.

I found `rust` one of the most invovled languages to learn. Like many people I have learnt, to varying degrees, many languages over the years: BASIC, Pascal, FORTRAN, C, C#, Python, F#, lisp, haskell and Javascript to name a few. `rust` takes a long time to get aquantied with because of the unfamiliar concepts of how to manage memory really effectively (with `C` and `C++` you can get going leaving memory, and thus security, issues in your wake) I had a head start with the static typing and functional aspects owing to the fact that I had learnt `ml` langagues earlier. Learning `rust` is comparable to learning a functional language (`F#`, `lisp`) for the first time as the concepts are not like mainstream programming langagues with their reliance on procedures and classes. If you've only used `REPL` languages like `Python` you are in for a shock when you try a compiled strongly-typed language like `rust`.

I don't consider `rust` difficult to learn but it does take much, much longer to start real programming by yourself. Contrast this with `Python` which is easy to start programming and then descends into a morass of libraies, virutalisation and package management. Spreadsheets are also an easy entry to programming with data front and centre. Spreadsheets soon become an impossible change-management problem with their plethora of easily modified and obscured functions. There are banks that have banned spreadsheets from certain parts of their business owing to this complexity and lack of control.

## See also

[Fornjot is an early-stage CAD kernel](https://github.com/hannobraun/fornjot)

[Rust Beginnings](/docs/rust/2023-03-16-Rust-Beginnings.md) needs to be moved from here, and deleted in beginning rust

## Links

* [toml crate](https://docs.rs/toml/latest/toml/)
