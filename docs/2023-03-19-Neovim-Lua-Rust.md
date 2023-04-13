---
date: "2023-03-19"
title: "Neovim-Lua-Rust"
---
<!-- markdownlint-disable MD025 -->
# Neovim-Lua-Rust
<!-- markdownlint-enable MD025 -->

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

## Vim, Neovim and Related

* [unicode.vim](https://github.com/chrisbra/unicode.vim)
* [Your problem with Vim is that you don't grok vi](https://stackoverflow.com/a/1220118/3617057)

Probably the most important command

```vim
:h quickref
```
* [Building Neovim](https://github.com/neovim/neovim/wiki/Building-Neovim)
* [Neovim from Scratch playlist - YouTube](https://www.youtube.com/playlist?list=PLhoH5vyxr6Qq41NFL4GvhFp-WLd5xzIzZ)
* [Awesome Neovim](https://github.com/rockerBOO/awesome-neovim#file-explorer)
* [julia-vim](https://github.com/JuliaEditorSupport/julia-vim/blob/master/INSTALL.md)
* [LunarVimConfig for Julia](https://github.com/davibarreira/LunarVimConfig)

"nikvdp/neomux" needs the terminal number

```vim
:lua print(vim.api.nvim_eval("tabpagewinnr(tabpagenr())"))
-- or
:lua print(vim.api.nvim_eval("winnr()"))
-- or
:lua print(vim.fn.winnr())
```

run

git clone the target nvim into a subdirectory of .config 
need the latest (9+) version of nvim

* [A Basic Stable IDE config for Neovim](https://github.com/LunarVim/nvim-basic-ide)
* [Neovim Config Switcher - Gist](https://gist.github.com/elijahmanor/b279553c0132bfad7eae23e34ceb593b) and [Neovim Config Switcher - YouTube](https://youtu.be/LkHjJlSgKZY)

```sh
alias nvim-lazy="NVIM_APPNAME=LazyVim nvim"
alias nvim-kick="NVIM_APPNAME=kickstart nvim"
alias nvim-chad="NVIM_APPNAME=LunarVim nvim"
alias nvim-astro="NVIM_APPNAME=AstroNvim nvim"

function nvims() {
  items=("default" "kickstart" "LazyVim" "LunarVim" "AstroNvim")
  config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)
  if [[ -z $config ]]; then
    echo "Nothing selected"
    return 0
  elif [[ $config == "default" ]]; then
    config=""
  fi
  NVIM_APPNAME=$config nvim $@
}

bindkey -s ^a "nvims\n"
```

```bash
nvim --listen ~/.cache/nvim/server.pipe
```
(the pipe name is arbitary)
in one instatance, can be used interactively. Then

```bash
nvim --server ~/.cache/nvim/server.pipe --remote-expr "winnr()"
```

* [Example init.lua etc](https://github.com/cpow/cpow-dotfiles)
* [Build your first Neovim configuration in lua](https://vonheikemen.github.io/devlog/tools/build-your-first-lua-config-for-neovim/)
* https://www.jackfranklin.co.uk/blog/executing-tasks-in-neovim/

* [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com)

* [Vim Cheat Sheet](https://vim.rtorr.com)
* [Home - Neovim](https://neovim.io)
* [AstroNvim is an aesthetic and feature-rich neovim](https://astronvim.com/#-features)
* [GitHub - neoclide/coc.nvim: Nodejs extension host for vim & neovim, load extensions like VSCode and host language servers.](https://github.com/neoclide/coc.nvim)
* [GitHub - dense-analysis/ale: Check syntax in Vim asynchronously and fix files, with Language Server Protocol (LSP) support](https://github.com/dense-analysis/ale)
* [Vim As an IDE for Python 2021](https://medium.com/nerd-for-tech/vim-as-an-ide-for-python-2021-f922da6d2cfe)
* [Vim for Python in 2020 | Vim From Scratch](https://www.vimfromscratch.com/articles/vim-for-python)
* [Vim - Full Stack Python](https://www.fullstackpython.com/vim.html)
* [VIM and Python – A Match Made in Heaven – Real Python](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
* [learnbyexample - vim](https://learnbyexample.github.io/tips/#vim)
* [Home - code-server Docs](https://coder.com/docs/code-server/latest)

## Vim, Neovim, nvim

Reset nvim

```sh
rm -rf ~/.cache/nvim
rm -rf ~/.local/share/nvim
rm -rf ./.config/nvim
```

[Build your first Neovim configuration in lua](https://vonheikemen.github.io/devlog/tools/build-your-first-lua-config-for-neovim/)

* [Why Neovim is the best code editor / IDE for developers](https://console.dev/articles/neovim-best-code-editor-ide-for-developers/)
* [Neovim and Rust · sharksforarms](https://sharksforarms.dev/posts/neovim-rust/)
* [GitHub - junegunn/vim-plug: Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [GitHub - hrsh7th/nvim-cmp: A completion plugin for neovim coded in Lua.](https://github.com/hrsh7th/nvim-cmp)

* [How to Configure Neovim to make it Amazing -- complete tutorial](https://youtu.be/J9yqSdvAKXY) with the [Github files here](https://github.com/cpow/cpow-dotfiles)
* [neovim configuration](https://youtu.be/J9yqSdvAKXY)
* [nvim-cmp](https://youtu.be/_DnmphIwnjo)
* [Intro to LuaSnips](https://youtu.be/Dn800rlPIho)
* [LuaSnips](https://youtu.be/KtQZRAkgLqo)
* [Automate with Lua in Neovim](https://youtu.be/9gUatBHuXE0)

## LaTeX

* [Compiling LaTeX Documents in a Vim-Based Workflow](https://www.ejmastnak.com/tutorials/vim-latex/compilation/)
* [VimTeX](https://github.com/lervag/vimtex)

## Lua

* [Learning Lua - resources](http://lua-users.org/wiki/LearningLua)
* [Programming in Lua : 1](http://www.lua.org/pil/1.html)
* [Lua for Programmers Part 1: Language Essentials](https://ebens.me/post/lua-for-programmers-part-1/)
* [lua - Rust](https://docs.rs/lua/latest/lua/)
* [GitHub - amethyst/rlua: High level Lua bindings to Rust](https://github.com/amethyst/rlua)
* [Learn Lua in Y Minutes](https://learnxinyminutes.com/docs/lua/)
* [Lua Unofficial FAQ (uFAQ)](https://www.luafaq.org)

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->

