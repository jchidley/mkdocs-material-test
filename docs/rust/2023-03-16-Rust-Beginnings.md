---
date: "2023-03-16"
title: "Rust-Beginnings"
---
<!-- markdownlint-disable MD025 -->
# Rust Beginnings
<!-- markdownlint-enable MD025 -->

## Introduction

* [Learn Rust](https://www.rust-lang.org/learn)
* [Command line apps in Rust](https://rust-cli.github.io/book/index.html)
* [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/index.html)
* [rustlings](https://rustlings.cool/)
* The Dark Arts of Unsafe Rust [The Rustonomicon](https://doc.rust-lang.org/stable/nomicon/intro.html)
* [The Rust FFI Omnibus is a collection of examples of using code written in Rust from other languages.](https://jakegoulding.com/rust-ffi-omnibus/)

## Install for Windows

*Build Tools for Visual Studio 2022* - look down the page [Downloads](https://visualstudio.microsoft.com/downloads/)

* MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)
* Windows 11 SDK (10.0.22621.0)

Then run `rustup-init.exe` from [Install Rust](https://www.rust-lang.org/tools/install)

```bash
rustup docs --book
```

### Speedup

use the [LLD linker](https://lld.llvm.org/) to speed it up.

### Rust-Analyzer

```PowerShell
(get-command rust-analyzer).Source # C:\Users\jackc\.cargo\bin\rust-analyzer.exe
curl -L -O https://github.com/rust-lang/rust-analyzer/releases/download/2024-02-12/rust-analyzer-x86_64-pc-windows-msvc.zip
copy .\rust-analyzer.exe (get-command rust-analyzer).Source
```

## Learning by Programming

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

see [Parsing-Compilers](/docs/Other/2021-07-06-Parsing-Compilers.md) and [Writing a Programming Language](/docs/2023-09-04-Writing-A-Programming-Language.md)

### Background
* [(How to Write a (Lisp) Interpreter (in Python))](http://www.norvig.com/lispy.html)
* [(An ((Even Better) Lisp) Interpreter (in Python))](http://norvig.com/lispy2.html)
* [Learning with Peter Norvig's lis.py interpreter](https://github.com/fluentpython/lispy)

### TOML

* [vim for Rust](https://blog.logrocket.com/configuring-vim-rust-development/)
* [Rust Load a TOML File](https://codingpackets.com/blog/rust-load-a-toml-file/)

## Helix

[helix-editor](/docs/2024-02-13-Helix.md)

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

* [Neovide](https://neovide.dev/index.html) - doesn't work that well on my Mac Book m

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
* [GitHub - rust-lang/rustlings: Small exercises to get you used to reading and writing Rust code!](https://github.com/rust-lang/rustlings/)
* [Introduction - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/)
* [The Rust Programming Language - The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)
* [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)
* [Frustrated? It's not you, it's Rust](https://fasterthanli.me/articles/frustrated-its-not-you-its-rust)
* [How to Mix Rust and Python in Your Project](https://medium.com/@MatthieuL49/a-mixed-rust-python-project-24491e2af424)
* [GitHub - PyO3/pyo3: Rust bindings for the Python interpreter](https://github.com/PyO3/pyo3)
* [Introduction - PyO3 user guide](https://pyo3.rs/)
* [Experiment Introduction - The Rust Programming Language](https://rust-book.cs.brown.edu)

## Rust and Neovim
 
* [rust - NeoVim shows diagnostic for `std` and other crates outside my current workspace - Stack Overflow](https://stackoverflow.com/questions/75544704/neovim-shows-diagnostic-for-std-and-other-crates-outside-my-current-workspace)
* [Rust and Neovim - A Thorough Guide and Walkthrough | the trait](https://rsdlt.github.io/posts/rust-nvim-ide-guide-walkthrough-development-debug/)
* [Neovim and Rust · sharksforarms](https://sharksforarms.dev/posts/neovim-rust/)
* [GitHub - Integralist/nvim: Neovim configuration](https://github.com/integralist/nvim)

* [lua - Rust](https://docs.rs/lua/latest/lua/)
* [GitHub - amethyst/rlua: High level Lua bindings to Rust](https://github.com/amethyst/rlua)

