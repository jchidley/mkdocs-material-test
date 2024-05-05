---
date: "2024-03-10"
title: "How-I-Learned-Rust"
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

```PowerhShell
cd $env:TEMP # Windows temporary directory
cargo new --lib rust_explore # almost all programming involves creating and using libraries
cargo test --lib tests -- --nocapture # `-- --nocapture` for `println!`` and friends
Set-ExecutionPolicy Unrestricted -Scope Process; iex (iwr "https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.ps1").Content # binary install for crates
cargo binstall cargo-watch # watcher
# open 3 panes: 1) `hx .\src\lib.rs` editor 2) `cargo watch -x check` hot-loading compile checking 3) `cargo test --lib explore -- --nocapture` or `cargo add some-crate` or some other command
```

I rename the module `tests` to `explore` and use that to explore the rust language as I'm learning it. 

I make sure that the test includes a `let result =` assigment directly before `dgb!{result);`. Once I am compfortable with this, I use the result in an appropriate `assert` macro for the final test.

This closely mimics my ideal development process. First I explore the libraries I might use and then I use tests as I develop the code. Sometimes its code first, sometimes its test first; I write documentation, including examples, at the same time. I aim for 100% coverage of the code with tests and documentation. I'd by lying if I wrote that I always do this.

Given that almost everyting that I do involves the command line I used [Command line apps in Rust](https://rust-cli.github.io/book/index.html) book as a reference implemetation and tutorial.

## Getting Started

I did a skim read of the [The Rust Programming Language](https://doc.rust-lang.org/stable/book/title-page.html), and watched [doggo dot rs](https://www.youtube.com/@doggodotrs)'s full rust course.

I followed this up with working my way through [rustlings](https://github.com/rust-lang/rustlings), Trevor Sullivan's [Rust Programming Tutorial](https://youtube.com/playlist?list=PLDbRgZ0OOEpUkWDGqp91ODn0dk7LPBAUL&si=sMPsWPC0eELRTf_5) and *Mastering Rust - Second Edition*
by *Rahul Sharma and Vesa Kaihlavirta* concurrently.

I found `rust` one of the most invovled languages to learn. Like many people I have learnt, to varying degrees, many languages over the years: BASIC, Pascal, FORTRAN, C, C#, Python, F#, lisp, haskell and Javascript to name a few. `rust` takes a long time to get aquantied with because of the unfamiliar concepts of how to manage memory really effectively (with `C` and `C++` you can get going leaving memory, and thus security, issues in your wake) I had a head start with the static typing and functional aspects owing to the fact that I had learnt `ml` langagues earlier. Learning `rust` is comparable to learning a functional language (`F#`, `lisp`) for the first time as the concepts are not like mainstream programming langagues with their reliance on procedures and classes. If you've only used `REPL` languages like `Python` you are in for a shock when you try a compiled strongly-typed language like `rust`.

I don't consider `rust` difficult to learn but it does take much, much longer to start real programming by yourself. Contrast this with `Python` which is easy to start programming and then descends into a morass of libraies, virutalisation and package management. Spreadsheets are also an easy entry to programming with data front and centre. Spreadsheets soon become an impossible change-management problem with their plethora of easily modified and obscured functions. There are banks that have banned spreadsheets from certain parts of their business owing to this complexity and lack of control.

## Embedded

* [Introduction to Rust programming on bare metal hardware by Mike Kefeder - Rust Zürisee March 2023](https://www.youtube.com/watch?v=KECu_piSM5s)
* [The Embedded Rust ESP Development Ecosystem](https://dev.to/apollolabsbin/embedded-rust-the-esp-development-ecosystem-5478)

[Fornjot is an early-stage CAD kernel](https://github.com/hannobraun/fornjot)


============= needs to be moved from here, and deleted in beginning rust

### Easy

* [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/index.html)
* [easy rust](https://dhghomon.github.io/easy_rust/Chapter_0.html)
* [Rust Programming Tutorial](https://youtube.com/playlist?list=PLDbRgZ0OOEpUkWDGqp91ODn0dk7LPBAUL&si=ieLsv_wfmKSBKGtO)
* [The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/introduction.html) is great to read as many books and examples now use older editions.
* [The Rust Reference](https://doc.rust-lang.org/stable/reference/)

### More involved

[Rust exercises on Exercism](https://exercism.org/tracks/rust/exercises)

Brown University's version of the [Rust Book](https://rust-book.cs.brown.edu/title-page.html) is best left as a revision work because it tries really, really hard to make sure that you've understood everything. I thought that this would be a perfect way to get started but, as I discovered, I became dishartened because I didn't understand everything perfectly and it is labourious to work through. Rust is quite a hard language to get to grips with because it forces you, the programmer, to write correct code. Writing correct code is hard.

* [Cargo B(inary)Install](https://github.com/cargo-bins/cargo-binstall) to install binary files using Cargo. Normally Cargo downloads the source files and complies them first.
* [This Week in Rust](https://this-week-in-rust.org/)
* [currently](https://this-week-in-rust.org/blog/2013/10/06/the-state-of-rust-08/)
* [Rewritten in Rust: Modern Alternatives of Command-Line Tools](https://zaiste.net/posts/shell-commands-rust/) is slightly out of date (e.g. `btm` replaces `ytop`) but still great to see what is possible.
* [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) - this reminds me of F#'s tutorial that, if I remember correctly, was included by default with Visual Studio or the .net example project for F#.
* The Dark Arts of Unsafe Rust [The Rustonomicon](https://doc.rust-lang.org/stable/nomicon/intro.html)
* [The Rust FFI Omnibus is a collection of examples of using code written in Rust from other languages.](https://jakegoulding.com/rust-ffi-omnibus/)

### Dead Tree, Live Bits

"[Zero To Production In Rust](https://www.zero2prod.com/) is the ideal starting point for your journey as a Rust backend developer. You will learn by doing: you will build a fully functional email newsletter API, starting from scratch."

[Rust in Action - Systems programming concepts and techniques](https://www.manning.com/books/rust-in-action) also has an accociated audiobook from Audible. Interesting to look at source code / companion pdf and listen to it. Requires more work to understand which is a good thing.

[Packt Publishing](https://www.packtpub.com/), [Manning](https://www.manning.com/) and the big dog [O’Reilly](https://www.oreilly.com/), and probably others, have libraries of both books and video courses.

[Rust in Motion](https://www.manning.com/livevideo/rust-in-motion) is a little outdated but still relevant, one of the presenters wrote the *rust book*.

## Install for Windows

*Build Tools for Visual Studio 2022* - look down the page [Downloads](https://visualstudio.microsoft.com/downloads/), then install these two bits of software:

* MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)
* Windows 11 SDK (10.0.22621.0)

Run `rustup-init.exe` from [Install Rust](https://www.rust-lang.org/tools/install)

### rustup

* [The rustup book](https://rust-lang.github.io/rustup/index.html)

```bash
rustup docs --book
```

```Powershell
rustup target list # cross-compile options
# cargo build --target=arm-linux-androideabi # for example
rustup completions powershell >> $PROFILE.CurrentUserCurrentHost # The included using statements belong at the top of $PROFILE 
```

### Speedup

use the [LLD linker](https://lld.llvm.org/) to speed it up.

### Rust-Analyzer

If you have installed rust-analyzer via rustup _do not_ update it standalone, nor the other way around.

#### From Source

Initial Instllation:

```shell
git clone https://github.com/rust-lang/rust-analyzer.git
cd rust-analyzer
git checkout release # master is also an option
cargo xtask install --server # standalone client
```

Update:

```shell
cd rust-analyzer
git pull
cargo xtask install --server # standalone client
```

#### From Releases 

Install:

* Download a suitable Windows specific release e.g. `rust-analyzer-x86_64-pc-windows-msvc.zip`
* Extract the files
* Copy the `rust-analyzer.exe` file to a suitable directory (e.g. `C:\tools`)
* Add that directory to the user's *path* _environmental variable_
* Open a new `Command Prompt` or `PowerShell` to use `rust-analyzer` 

Update:

```PowerShell
(get-command rust-analyzer).Source # c:\tools # for example
curl -L -O https://github.com/rust-lang/rust-analyzer/releases/download/2024-02-12/rust-analyzer-x86_64-pc-windows-msvc.zip # check current version
copy .\rust-analyzer.exe (get-command rust-analyzer).Source
```

#### rustup

## String, str, u8

Rust is going to try pretty hard to make sure that these are valid conversions. Strings convert to u8 (bytes) in very specific ways. Ways that include variable multi-byte encoding.

[How do I convert between String, &str, Vec\<u8\> and &\[u8\]](https://stackoverflow.com/a/41034751/3617057)

```code
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

* target should have explicit type (i.e., checker can't infer that)

** handle the error properly instead
```

There are also these other functions, and probably more too.
 
```rust
std::str::from_utf8_unchecked
std::string::String::from_utf8
String::from_utf8_lossy
```

Sometimes you just want to the type [see Boiethios's Stackoverflow answer](https://stackoverflow.com/a/58119924/3617057) or [fasterthanli.me's use of type_name](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)

```rust
use std::any::type_name;

fn main() {
    let x = &false;
    print_type_name_of(&x);

    let ref x = &false;
    print_type_name_of(&x);

    let x = 1.0;
    print_type_name_of(&x);
}

fn print_type_name_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}
```

To find out what your type, defined in your libraries not `main.rs`, implements:

`cargo doc --open # --document-private-items # for private types too`

### Documenting

* [The rustdoc book](https://doc.rust-lang.org/rustdoc/index.html)
* [mdBook is a command line tool to create books with Markdown](https://rust-lang.github.io/mdBook/)

## Learning by Programming

### Exercises in Programming Style

[Exercises in Programming Style](https://github.com/crista/exercises-in-programming-style) by Crista, who wrote a book of the same name, which I own on Kindle.

[F# port of the examples in "Exercises in Programming Style"](https://github.com/theburningmonk/exercises-in-programming-style-fsharp), starting with [Exercises in Programming Style–Style 1](https://theburningmonk.com/2015/08/exercises-in-programming-stylestyle-1/), [Exercises in Programming Style–Go Forth](https://theburningmonk.com/2015/09/exercises-in-programming-stylestyle-2/) for more try [this search](site:https://theburningmonk.com/ "Exercises in programming style")

### Games

* convert this [Learn To Code Space Invaders – learn lua by programming](https://bytesnbits.co.uk/space-invaders-coding-course-introduction/) from lua to [Rust and WebAssembly](https://rustwasm.github.io/docs/book/introduction.html) using this [WASM-4 fantasy game console](https://wasm4.org/docs/)

[Bevy - lots of coding](https://youtu.be/TQt-v_bFdao?si=BN7cSQz-7h3_8bb5)
[Bevy - 3rd from scratch series - Farming Robot](https://youtu.be/NysHtgLxOtU?si=Cb7dWNhmaqNbNP1_)
[Bevy (half exposition and half coding) - Asteroids?](https://youtu.be/B6ZFuYYZCSY?si=BcmYx9i6vZfvr9VZ)
[Rust Bevy - Space Invaders](https://youtu.be/j7qHwb7geIM?si=ZRJLgTpEOCN2ZIW8)

### Programming Language

* [mal - Make a Lisp](https://github.com/kanaka/mal?tab=readme-ov-file#rust-138)
* [Rust Your Own Lisp](https://dev.to/deciduously/rust-your-own-lisp-50an) from the book [Build Your Own Lisp](https://www.buildyourownlisp.com/)
* Write a C compiler by converting this [chibicc](https://github.com/rui314/chibicc) and then doing this version [chibicc-riscv](https://github.com/ksco/chibicc-riscv)

see [Parsing-Compilers](docs/Other/2021-07-06-Parsing-Compilers.md) and [Writing a Programming Language](docs/2023-09-04-Writing-A-Programming-Language.md)

### Background
* [(How to Write a (Lisp) Interpreter (in Python))](http://www.norvig.com/lispy.html)
* [(An ((Even Better) Lisp) Interpreter (in Python))](http://norvig.com/lispy2.html)
* [Learning with Peter Norvig's lis.py interpreter](https://github.com/fluentpython/lispy)

### TOML

* [vim for Rust](https://blog.logrocket.com/configuring-vim-rust-development/)
* [Rust Load a TOML File](https://codingpackets.com/blog/rust-load-a-toml-file/)

## Helix

[helix-editor](docs/2024-02-13-Helix.md)

```bash
rustup component add rust-analyzer // for this to work
```

## IDE

[pylint replacement with Ruff](https://github.com/charliermarsh/ruff/issues/970)

in `.pylintrc` file (or `pylintrc`, or...)

```pylint
pylint --extension-pkg-allow-list=your_c_extension
```

turn on mypy linting and then build a suitable `*.pyi` file to contain the definitions. To do that search for `mypy linting` in the VS Code settings (user and workspace).

* [Neovide](https://neovide.dev/index.html) - doesn't work that well on my Mac Book m1

## With Python

* [PyO3 user guide](https://pyo3.rs/)
* [Maturin User Guide](https://www.maturin.rs)

* [Using Pylint with PyModule generated using PyO3 and maturin](https://stackoverflow.com/questions/73861487/using-pylint-with-pymodule-generated-using-pyo3-and-maturin)

* [Type Stubs](https://typing.readthedocs.io/en/latest/source/stubs.html)
* [Creating Stubs For Python Modules](https://github.com/python/mypy/wiki/Creating-Stubs-For-Python-Modules)

```python
def sum_as_string(a: int, b: int) -> str: ...
```

## Links

<!-- markdownlint-disable MD034 -->
* https://docs.rs/toml/latest/toml/
<!-- markdownlint-enable MD034 -->
* [The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)
* [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/intro.html)

## Rust

* [Rust Programming Language](https://www.rust-lang.org)
* [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)
* [Frustrated? It's not you, it's Rust](https://fasterthanli.me/articles/frustrated-its-not-you-its-rust)
* [How to Mix Rust and Python in Your Project](https://medium.com/@MatthieuL49/a-mixed-rust-python-project-24491e2af424)
* [GitHub - PyO3/pyo3: Rust bindings for the Python interpreter](https://github.com/PyO3/pyo3)
* [Introduction - PyO3 user guide](https://pyo3.rs/)

## Rust and Neovim
 
* [rust - NeoVim shows diagnostic for `std` and other crates outside my current workspace - Stack Overflow](https://stackoverflow.com/questions/75544704/neovim-shows-diagnostic-for-std-and-other-crates-outside-my-current-workspace)
* [Rust and Neovim - A Thorough Guide and Walkthrough | the trait](https://rsdlt.github.io/posts/rust-nvim-ide-guide-walkthrough-development-debug/)
* [Neovim and Rust · sharksforarms](https://sharksforarms.dev/posts/neovim-rust/)
* [GitHub - Integralist/nvim: Neovim configuration](https://github.com/integralist/nvim)

* [lua - Rust](https://docs.rs/lua/latest/lua/)
* [GitHub - amethyst/rlua: High level Lua bindings to Rust](https://github.com/amethyst/rlua)
