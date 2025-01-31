---
date: "2023-03-16"
title: "Rust-Beginnings"
---
<!-- markdownlint-disable MD025 -->
# Rust Beginnings
<!-- markdownlint-enable MD025 -->

## Introduction

### Easy

* [Learn Rust](https://www.rust-lang.org/learn)
* [rustlings](https://rustlings.cool/)
* [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/index.html)
* [easy rust](https://dhghomon.github.io/easy_rust/Chapter_0.html)
* [Rust Programming Tutorial](https://youtube.com/playlist?list=PLDbRgZ0OOEpUkWDGqp91ODn0dk7LPBAUL&si=ieLsv_wfmKSBKGtO)
* [The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/introduction.html) is great to read as many books and examples now use older editions.
* [The Rust Reference](https://doc.rust-lang.org/stable/reference/)
* [Rust Design Patterns](https://rust-unofficial.github.io/patterns/intro.html)

### More involved

[Rust exercises on Exercism](https://exercism.org/tracks/rust/exercises)
[C2Rust](https://github.com/immunant/c2rust?tab=readme-ov-file)
[Citrus: Convert C to Rust](https://gitlab.com/citrus-rs/citrus)

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

[Rust for Rustaceans](https://nostarch.com/rust-rustaceans#reviews)

[Rust in Action - Systems programming concepts and techniques](https://www.manning.com/books/rust-in-action) also has an accociated audiobook from Audible. Interesting to look at source code / companion pdf and listen to it. Requires more work to understand which is a good thing.

[Packt Publishing](https://www.packtpub.com/), [Manning](https://www.manning.com/) and the big dog [O’Reilly](https://www.oreilly.com/), and probably others, have libraries of both books and video courses.

[Rust in Motion](https://www.manning.com/livevideo/rust-in-motion) is a little outdated but still relevant, one of the presenters wrote the *rust book*.

[Roguelike Tutorial - In Rust](https://bfnightly.bracketproductions.com/rustbook/chapter_0.html)

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

## String, str, u8

See [Unicode, Strings, str, char, u8](./2024-05-05-Rust-General.md)

Rust uses ut8 encoding for strings, etc, chars are u32 which is the size of [Unicode Scalar Value](https://unicode.org/glossary/#unicode_scalar_value) but characters are just a number known as a [Code point: Any value in the Unicode codespace.](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G22700). For some langauges characters can be made up of several code points. [Unicode® Standard Annex #29](https://www.unicode.org/reports/tr29/) 

## Types

[Sometimes you just want to the type [see Boiethios's Stackoverflow answer](https://stackoverflow.com/a/58119924/3617057) or [fasterthanli.me's use of type_name](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)

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
