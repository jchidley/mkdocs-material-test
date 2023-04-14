---
date: "2023-04-14"
title: "Neovim-Lua"
---
<!-- markdownlint-disable MD025 -->
# Neovim Lua
<!-- markdownlint-enable MD025 -->

## Vim, Neovim and Related

* [unicode.vim](https://github.com/chrisbra/unicode.vim)
* [Your problem with Vim is that you don't grok vi](https://stackoverflow.com/a/1220118/3617057)

Probably the most important command

```vim
:h quickref
```

### Toggleterm 

for LazyVim 


print the full path 
```sh
find "$(pwd -P)" -name "filename"
```
```sh
cat << EOF >.config/LazyVim/lua/plugins/toggleterm.lua
return {
  {
    "akinsho/toggleterm.nvim",
    version = "*",
    opts = {--[[ things you want to change go here]]
      open_mapping = [[<c-\><c-\>]],
      hide_numbers = false,
      direction = "vertical",
      size = function(term)
        if term.direction == "horizontal" then
          return 15
        elseif term.direction == "vertical" then
          return vim.o.columns * 0.4
        end
      end,
    },
  },
}
EOF
```
You can "send lines" to the toggled terminals with the following commands:

* :ToggleTermSendCurrentLine <T_ID>: sends the whole line where you are standing with your cursor
* :ToggleTermSendVisualLines <T_ID>: sends all the (whole) lines in your visual selection
* :ToggleTermSendVisualSelection <T_ID>: sends only the visually selected text (this can be a block of text or a selection in a single line)

(<T_ID is an optional terminal ID parameter, which defines where should we send the lines. If the parameter is not provided, then the default is the first terminal)


* [Building Neovim](https://github.com/neovim/neovim/wiki/Building-Neovim)
* [Neovim from Scratch playlist - YouTube](https://www.youtube.com/playlist?list=PLhoH5vyxr6Qq41NFL4GvhFp-WLd5xzIzZ)
* [Awesome Neovim](https://github.com/rockerBOO/awesome-neovim#file-explorer)
* [julia-vim](https://github.com/JuliaEditorSupport/julia-vim/blob/master/INSTALL.md)
* [LunarVimConfig for Julia](https://github.com/davibarreira/LunarVimConfig)

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

funtcion nvims() {
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

(the pipe name is arbitrary)
in one instance, can be used interactively. Then

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

* [Build your first Neovim configuration in lua](https://vonheikemen.github.io/devlog/tools/build-your-first-lua-config-for-neovim/)
* [Why Neovim is the best code editor / IDE for developers](https://console.dev/articles/neovim-best-code-editor-ide-for-developers/)
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
* [Learn Lua in Y Minutes](https://learnxinyminutes.com/docs/lua/)
* [Lua Unofficial FAQ (uFAQ)](https://www.luafaq.org)

