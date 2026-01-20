---
date: "2023-04-14"
title: "Neovim Lua"
tags:
  - editor
  - neovim
  - lua
  - programming
  - tools
---
<!-- markdownlint-disable MD025 -->
# Neovim Lua
<!-- markdownlint-enable MD025 -->

`vi` isn't easy to learn. It's keyboard driven and there is next to no visual
help. Even modern variants, like `neovim`, don't give you on-screen clues. It
is easier to pick up things are are visual - Atom, VS Code, etc, but those
tools make the easy things easier and the hard things harder. In the end, if
you are serious about editing effectively, you will have to be an expert in
the tools for job. There are no substitutes.

So, sure, if you are a beginner and want to get started, pick the easiest tool
because everything is hard to begin with. But as soon as you are at the
intermediate level, it's time to pick up the expert's tools. It's time to put
in the hard work. You'll be better for it.

Neovim is text editing equivalent of touch typing. It seems impossible at the
start. But soon enough, much sooner than you think, you'll be typing at over
60 words-per-minute just looking at the screen, thinking about what you are
writing. You will not be looking at the keyboard typing at 30 words-per-minute
and making loads of semantic and syntactic mistakes. It's the same for `vi`
(and especially true for `neovim`) you'll be editing text quickly and
effectively from the keyboard. A mouse is a bonus. This is why touch-typing
and `vi` go hand-in-hand.

So dive into `neovim`. Learn the experts tool. It'll help make you an expert.
Learning to be an expert requires you to solve loads of problems. Have fun with
them.

## Moving to a new machine

You can definitely copy your configuration to a new machine but you still need
to install all the prerequisites for your various plugins.

### Windows

```PowerShell
choco install mingw # or # scoop install gcc # or # scoop install llvm
scoop bucket add nerd-fonts
scoop install sourcecodepro-nf
```

### Windows terminal

PowerShell 7
Settings → “Startup” → “Default profile”:  select "PowerShell"

See `2024-01-17-Microsoft-Surface-Laptop-4.md` for scoop install, including
nerd fonts.

```shell
C:\Users\jackc\git\mkdocs-material-test\docs\2024-01-17-Microsoft-Surface-Laptop-4.md
```

Nerd Font
Settings → “PowerShell” profile → “Appearance” → “Font face”: select Nerd Font

### Alacritty

Set "Start In" to %USERPROFILE% for the Alacritty shortcut on Windows

[Alacritty - TOML configuration file](https://alacritty.org/config-alacritty.html)

```PowerShell
nvim $env:APPDATA\alacritty\alacritty.toml
[font]
normal = { family = "SauceCodePro Nerd Font", style = "Regular" }
```

## Vim, Neovim and Related

* [unicode.vim](https://github.com/chrisbra/unicode.vim)
* [Your problem with Vim is that you don't grok vi](https://stackoverflow.com/a/1220118/3617057)

Probably the most important command

```vim
:h quickref
```

I added these to my `options.lua` file, see `:help option-list`

```lua
local opt = vim.opt
opt.wrap = true
-- enable soft wrapping at the edge of the screen
opt.linebreak = true
-- make it not wrap in the middle of a "word"
opt.colorcolumn = "80"
-- highlight when you go over a desired width
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
-- set tabs to 4 spaces
```

### Toggleterm

This is used to set the program for `:!` commands. It's also used for the terminal.

```vim
set shell=powershell
set shellcmdflag=-command
set shellquote=\"
set shellxquote=
```

[Change the default shell](https://superuser.com/questions/1759700/change-default-shell-to-powershell-in-neovim)
[Some vimrc options, including spell check](https://robindouglas.uk/powershell/vim/2018/04/05/PowerShell-with-Vim.html)
`set spell spelllang=en_gb`

for LazyVim

[Vim terminal: how powerful is it really?](https://www.reddit.com/r/vim/comments/goifnv/vim_terminal_how_powerful_is_it_really/)
print the full path from the command prompt

```bash
find "$(pwd -P)" -name "filename"
```

(from within `vim` its `:echo expand('%:p')` )

then use `gf` on that line (once you have switched to Normal mode) to open the file.

```lua
cat << EOF > ~/.config/LazyVim/lua/plugins/toggleterm.lua
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

* `:ToggleTermSendCurrentLine <T_ID>`: sends the whole line where you are
standing with your cursor
* `:ToggleTermSendVisualLines <T_ID>`: sends all the (whole) lines in your
visual selection
* `:ToggleTermSendVisualSelection <T_ID>`: sends only the visually selected
text (this can be a block of text or a selection in a single line)

(<T_ID is an optional terminal ID parameter, which defines where should we send the
lines. If the parameter is not provided, then the default is the first terminal)

Also, ^z (c-z), to exit vim temporarily and `fg` to go back

[From Vim and Tmux to Neovim](https://rutar.org/writing/from-vim-and-tmux-to-neovim/)

### Saving session state

LazyVim uses [persistence.nvim](https://github.com/folke/persistence.nvim) so
obsession.vim may not be needed but persistence.vim does not, by default,
automatically open the last session.

Use [obsession.vim](https://github.com/tpope/vim-obsession) (`:Obsess` to start/stop
recording) and then the state is retained, provided you use `-S` option on
startup (otherwise use `:source`) `:wa` to write all of your files and `ZZ` to
quit. By default, this will be saved in the directory where you started it.

`1<C-g>` for full path or `:echo expand('%:p')`. `<C-r>` in insert mode to add things
(including filnames, `%`) at the current cursor position or `"%p` in normal mode.

using `:Mason` to add `codespell` as a LSP and then `]s` to move between misspelled
words and `<leader>z=` to correct mistakes. Or install codespell (via pip) from the
command line and do it that way.

```bash
cat << EOF > ~/.config/LazyVim/lua/plugins/obsession.lua
return {
    -- vim session management with obsession.vim
    { "tpope/vim-obsession" },
}
EOF
```

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
* [Neovim Config Switcher - Gist](https://gist.github.com/elijahmanor/b279553c0132bfad7eae23e34ceb593b)
and [Neovim Config Switcher - YouTube](https://youtu.be/LkHjJlSgKZY)

```bash
alias nvim-lazy="NVIM_APPNAME=Lazy nvim -S"
alias nvim-kick="NVIM_APPNAME=kickstart nvim -S"
alias nvim-chad="NVIM_APPNAME=LunarVim nvim -S"
alias nvim-astro="NVIM_APPNAME=AstroNvim nvim -S"

funtcion nvims() {
  items=("default" "kickstart" "Lazy" "LunarVim" "AstroNvim")
  config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)
  if [[ -z $config ]]; then
    echo "Nothing selected"
    return 0
  elif [[ $config == "default" ]]; then
    config=""
  fi
  NVIM_APPNAME=$config nvim -S $@
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
* [Running command line tasks in Neovim](https://www.jackfranklin.co.uk/blog/executing-tasks-in-neovim/)

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

```bash
rm -rf ~/.cache/nvim
rm -rf ~/.local/share/nvim
rm -rf ./.config/nvim
```

* [Build your first Neovim configuration in lua](https://vonheikemen.github.io/devlog/tools/build-your-first-lua-config-for-neovim/)
* [Why Neovim is the best code editor / IDE for developers](https://web.archive.org/web/20240102131848/https://console.dev/articles/neovim-best-code-editor-ide-for-developers)
* [GitHub - junegunn/vim-plug: Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [GitHub - hrsh7th/nvim-cmp: A completion plugin for neovim coded in Lua.](https://github.com/hrsh7th/nvim-cmp)
* [How to Configure Neovim to make it Amazing -- complete tutorial](https://youtu.be/J9yqSdvAKXY)
with the [Github files here](https://github.com/cpow/cpow-dotfiles)
* [neovim configuration](https://youtu.be/J9yqSdvAKXY)
* [nvim-cmp](https://youtu.be/_DnmphIwnjo)
* [Intro to LuaSnips](https://youtu.be/Dn800rlPIho)
* [LuaSnips](https://youtu.be/KtQZRAkgLqo)
* [Automate with Lua in Neovim](https://youtu.be/9gUatBHuXE0)

## Julia

It's worth metioning that Juila is buit around pacakges as *the*
coding/development unit. Best to start with a minimal Pkg (`generate`) and work
from that. Testing will be easier too.

From this [Neovim + LanguageServer.jl discourse](https://discourse.julialang.org/t/neovim-languageserver-jl/37286)
and [Language server - missing references](https://discourse.julialang.org/t/language-server-missing-references/88936/19)

"
[neovim/nvim-lspconfig#1153](https://github.com/neovim/nvim-lspconfig/pull/1153)
is merged now so things should work out of the box if you:

Install LanguageServer in the shared environment ~/.julia/environments/nvim-lspconfig:

```bash
julia --project=~/.julia/environments/nvim-lspconfig -e 'using Pkg; Pkg.add("LanguageServer")'
```

I put this at the bottom of `init.lua` but it might belong somewhere else:

```lua
-- Julia LSP (LanguageServer.jl)
require'lspconfig'.julials.setup({
    on_new_config = function(new_config, _)
        local julia = vim.fn.expand("~/.julia/environments/nvim-lspconfig/bin/julia")
        new_config.cmd[1] = julia
    end,
    -- This just adds dirname(fname) as a fallback (see nvim-lspconfig#1768).
    root_dir = function(fname)
        local util = require'lspconfig.util'
        return util.root_pattern 'Project.toml'(fname) or util.find_git_ancestor(fname) or
               util.path.dirname(fname)
    end,
    on_attach = function(client, bufnr)
        on_attach(client, bufnr)
        -- Disable automatic formatexpr since the LS.jl formatter isn't so nice.
        vim.bo[bufnr].formatexpr = ''
    end,
    capabilities = capabilities,
})
```

```bash
curl https://raw.githubusercontent.com/fredrikekre/.dotfiles/master/.julia/environments/nvim-lspconfig/Makefile -o ~/.julia/environments/nvim-lspconfig/Makefile
cd ~/.julia/environments/nvim-lspconfig
make
```

Go into nvim, open a julia file, wait until the `julials` has loaded.

if the above doesn't work, then ...

I used [.julia/environments/nvim-lspconfig/Makefile](https://raw.githubusercontent.com/fredrikekre/.dotfiles/master/.julia/environments/nvim-lspconfig/Makefile)
file which I imported into this document using `:read`

<!-- markdownlint-disable MD010 -->
```bash
cat << EOF > ~/.julia/environments/nvim-lspconfig/Makefile
# MIT License. Copyright (c) 2021 Fredrik Ekre
#
# This Makefile can be used to build a custom Julia system image for LanguageServer.jl to
# use with neovims built in LSP support. An up-to date version of this Makefile can be found
# at https://github.com/fredrikekre/.dotfiles/blob/master/.julia/environments/nvim-lspconfig/Makefile
#
# Usage instructions:
#
#   1. Update the neovim configuration to use a custom julia executable. If you use
#      nvim-lspconfig (recommended) you can modify the setup call to the following:
#
#          require("lspconfig").julials.setup({
#              on_new_config = function(new_config, _)
#                  local julia = vim.fn.expand("~/.julia/environments/nvim-lspconfig/bin/julia")
#                  if require("lspconfig").util.path.is_file(julia) then
#                      new_config.cmd[1] = julia
#                  end
#              end,
#              -- ...
#          })
#
#   2. Place this Makefile in ~/.julia/environments/nvim-lspconfig (create the directory if
#   4. Upon exiting neovim PackageCompiler.jl will compile a custom system image which will
#      it doesn't already exist).
#
#      start up neovim in a custom project with a julia process that recods compiler
#      statements. Follow the instructions in the opened source file, and then exit neovim.
#
#      automatically be used whenever you work on Julia projects in neovim.
#
# Update instructions:
#
#  To update the system image (e.g. when upgrading Julia or upgrading LanguageServer.jl or
#   3. Change directory to ~/.julia/environments/nvim-lspconfig and run `make`. This will
#  it's dependencies) run the following commands from the
#  ~/.julia/environments/nvim-lspconfig directory:
#
#      julia --project=. -e 'using Pkg; Pkg.update()'
#      make

JULIA ?= $(shell which julia)
JULIA_PROJECT=
SRCDIR:=$(shell dirname $(abspath $(firstword $(MAKEFILE_LIST))))
ifeq ($(shell uname -s),Linux)
	SYSIMAGE=languageserver.so
else
	SYSIMAGE=languageserver.dylib
endif

default: $(SYSIMAGE)

$(SYSIMAGE): Manifest.toml packagecompiler/Manifest.toml packagecompiler/precompile_statements.jl
	JULIA_LOAD_PATH=${PWD}:${PWD}/packagecompiler:@stdlib ${JULIA} -e 'using PackageCompiler; PackageCompiler.create_sysimage(:LanguageServer, sysimage_path="$(SYSIMAGE)", precompile_statements_file="packagecompiler/precompile_statements.jl")'

Manifest.toml: Project.toml
	JULIA_LOAD_PATH=${PWD}/Project.toml:@stdlib ${JULIA} -e 'using Pkg; Pkg.instantiate()'

Project.toml:
	JULIA_LOAD_PATH=${PWD}/Project.toml:@stdlib ${JULIA} -e 'using Pkg; Pkg.add("LanguageServer")'

packagecompiler/Manifest.toml: packagecompiler/Project.toml
	JULIA_LOAD_PATH=${PWD}/packagecompiler/Project.toml:@stdlib ${JULIA} -e 'using Pkg; Pkg.instantiate()'

packagecompiler/Project.toml:
	mkdir -p packagecompiler
	JULIA_LOAD_PATH=${PWD}/packagecompiler/Project.toml:@stdlib ${JULIA} -e 'using Pkg; Pkg.add("PackageCompiler")'

packagecompiler/precompile_statements.jl: Manifest.toml bin/julia
	TMPDIR=$(shell mktemp -d) && \
	cd $${TMPDIR} && \
	JULIA_LOAD_PATH=: ${JULIA} -e 'using Pkg; Pkg.generate("Example")' 2> /dev/null && \
	cd Example && \
	JULIA_LOAD_PATH=$${PWD}:@stdlib ${JULIA} -e 'using Pkg; Pkg.add(["JSON", "fzf_jll", "Random", "Zlib_jll"])' 2> /dev/null && \
	JULIA_LOAD_PATH=$${PWD}:@stdlib ${JULIA} -e 'using Pkg; Pkg.precompile()' 2> /dev/null && \
	echo "$$PACKAGE_CONTENT" > src/Example.jl && \
	JULIA_TRACE_COMPILE=1 nvim src/Example.jl && \
	rm -rf $${TMPDIR}

bin/julia:
	mkdir -p bin
	echo "$$JULIA_SHIM" > $@
	chmod +x $@

clean:
	rm -rf $(SYSIMAGE) packagecompiler bin

.PHONY: clean default

export JULIA_SHIM
define JULIA_SHIM
#!/bin/bash
JULIA=${JULIA}
if [[ $${JULIA_TRACE_COMPILE} = "1" ]]; then
    exec $${JULIA} --trace-compile=${PWD}/packagecompiler/precompile_statements.jl "$$@"
elif [[ -f ${PWD}/$(SYSIMAGE) ]]; then
    exec $${JULIA} --sysimage=${PWD}/$(SYSIMAGE) "$$@"
else
    exec $${JULIA} "$$@"
fi
endef

export PACKAGE_CONTENT
define PACKAGE_CONTENT
# This file is opened in neovim with a LanguageServer.jl process that records Julia
# compilation statements for creating a custom sysimage.
#
# This file has a bunch of linter errors which will exercise the linter and record
# statements for that. When the diagnostic messages corresponding to those errors show up in
# the buffer the language server should be ready to accept other commands (note: this may
# take a while -- be patient). Here are some suggestions for various LSP functionality that
# can be exercised (your regular keybindings should work):
#
#  - :lua vim.lsp.buf.hover()
#  - :lua vim.lsp.buf.definition()
#  - :lua vim.lsp.buf.references()
#  - :lua vim.lsp.buf.rename()
#  - :lua vim.lsp.buf.formatting()
#  - :lua vim.lsp.buf.formatting_sync()
#  - :lua vim.lsp.buf.code_action()
#  - Tab completion (if you have set this up using LSP)
#  - ...
#
# When you are finished, simply exit neovim and PackageCompiler.jl will use all the recorded
# statements to create a custom sysimage. This sysimage will be used for the language server
# process in the future, and should result in almost instant response.

module Example

import JSON
import fzf_jll
using Random
using Zlib_jll

function hello(who, notused)
    println("hello", who)
    shuffle([1, 2, 3])
   shoffle([1, 2, 3])
    fzzf = fzf_jll.fzzf()
    fzf = fzf_jll.fzf(1)
    JSON.print(stdout, Dict("hello" => [1, 2, 3]), 2, 123)
    JSON.print(stdout, Dict("hello" => [1, 2, 3]))
    hi(who)
    return Zlib_jll.libz
end

function world(s)
    if s == nothing
      hello(s)
  else
      hello(s)
  end
    x = [1, 2, 3]
    for i in 1:length(x)
        println(x[i])
    end
end

end # module
endef
```
<!-- markdownlint-enable MD010 -->

```bash
cd ~/.julia/environments/nvim-lspconfig
make
```

Wait until after `julials` has finished before exiting neovim.

[Julia Language Server Configuration](https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md#julials) - may, or may not, be necessary.

[Julia VS Code Extension](https://github.com/julia-vscode/julia-vscode)

May also want [julia-vim](https://github.com/JuliaEditorSupport/julia-vim)

Might need to do this `julia -e 'using Pkg; Pkg.add("LanguageServer"); Pkg.add("SymbolServer")')`
if this hasn't been added to `nvim-lspconfig` already.

Need to add julia to treesitter too.

## Fugative Vim

`~/.config/nvim/lua/plugins/fugitive.lua`

```lua
return {
  { "tpope/vim-fugitive" },
}
```

"You may execute :Gw! command in any of the opened windows. The window where
you execute that command will be committed and marked as a merge resolution. It
is very useful if you want to use just REMOTE or just LOCAL version without any
further merge resolution steps.

Want more? When in the central window use d2o or d3o to pull changes from LOCAL
or REMOTE file."

See also [Neovim As Git Mergetool](https://smittie.de/posts/git-mergetool/)
for another version (although this doesn't seem to work for me)

[details about vimdiff & nvim](https://jdhao.github.io/2021/10/24/diff_in_vim/)

[Github integration for fugative.vim](https://github.com/tpope/vim-rhubarb)

[vim-gitgutter](https://github.com/airblade/vim-gitgutter) for see changes.

As recommended on the Fugative Github.

* [A complement to command line git](http://vimcasts.org/e/31)
* [Working with the git index](http://vimcasts.org/e/32)
* [Resolving merge conflicts with vimdiff](http://vimcasts.org/e/33)
* [Browsing the git object database](http://vimcasts.org/e/34)
* [Exploring the history of a git repository](http://vimcasts.org/e/35)

Other useful links

* [Git workflow using Neovim's Fugitive, Telescope & Git-Signs](https://www.youtube.com/watch?v=IyBAuDPzdFY)
* [Resolve Git Merge Conflicts with Neovim and Fugitive!](https://www.youtube.com/watch?v=vpwJ7fqD1CE)
* [Vim Plugin: Fugitive](https://www.youtube.com/watch?v=uUrKrYCAl1Y)
* [Two keys -= to transform your Git workflow #vim-fugitive](https://www.youtube.com/watch?v=vtFXMni91Q4)
* [Git rebase --interactive | Vim Fugitive](https://www.youtube.com/watch?v=6hude7CtBKg)

## LaTeX

* [Compiling LaTeX Documents in a Vim-Based Workflow](https://www.ejmastnak.com/tutorials/vim-latex/compilation/)
* [VimTeX](https://github.com/lervag/vimtex)

## Lua Plugin

[nvim-lua-plugin-template](https://github.com/nvim-lua/nvim-lua-plugin-template)
[How to write a neovim plugin in lua](https://miguelcrespo.co/posts/how-to-write-a-neovim-plugin-in-lua)
[Getting started using Lua in Neovim](https://github.com/nanotee/nvim-lua-guide)

## Lua

* [Learning Lua - resources](http://lua-users.org/wiki/LearningLua)
* [Programming in Lua : 1](http://www.lua.org/pil/1.html)
* [Lua for Programmers Part 1: Language Essentials](https://web.archive.org/web/20241121230629/https://ebens.me/post/lua-for-programmers-part-1/)
* [Learn Lua in Y Minutes](https://learnxinyminutes.com/docs/lua/)
* [Lua Unofficial FAQ (uFAQ)](https://www.luafaq.org)
* [Learn To Code Space Invaders – learn lua by programming](https://bytesnbits.co.uk/space-invaders-coding-course-introduction/)
* [External Editor for TIC-80](https://github.com/nesbox/TIC-80/wiki/External-Editor)
