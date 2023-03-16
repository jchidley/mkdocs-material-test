---
date: "2023-03-16"
title: "Rust-Beginnings"
---
<!-- markdownlint-disable MD025 -->
# Rust Beginnings
<!-- markdownlint-enable MD025 -->

## Introduction

* [Learn Rust](https://www.rust-lang.org/learn)

```bash
rustup docs --book
```

### TOML

* [vim for Rust](https://blog.logrocket.com/configuring-vim-rust-development/)
* [Rust Load a TOML File](https://codingpackets.com/blog/rust-load-a-toml-file/)

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
