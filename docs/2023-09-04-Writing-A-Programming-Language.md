---
date: "2023-09-04"
title: "Writing-A-Programming-Language"
---
<!-- markdownlint-disable MD025 -->
# Writing A Programming Language
<!-- markdownlint-enable MD025 -->

## Introduction

A sentence

## Front Ends

* [Lerche (German for Lark) is a partial port of the Lark grammar processor from Python to Julia](https://github.com/jamesrhester/Lerche.jl)
* [Lark - a parsing toolkit for Python](https://github.com/lark-parser/lark)
* [Automa is a regex-to-Julia compiler.](https://biojulia.dev/Automa.jl/previews/PR119/)
* [CombinedParsers in pure Julia](https://github.com/gkappler/CombinedParsers.jl)
* [AbstractTrees.jl](https://juliacollections.github.io/AbstractTrees.jl/stable/)
* [Trees in Julia](https://discourse.julialang.org/t/trees-in-julia/12173)
* [GraphMakie.jl In this example we are going to plot an abstract syntax tree of a Julia function using the Bucheim Layout from NetworkLayout.jl.](https://graph.makie.org/dev/generated/syntaxtree/)
* [Rex Eats Regular Expressions for Breakfast](https://www.rexegg.com/)

* [What LISP compilers and interpreters were available for 8-bit machines?](https://retrocomputing.stackexchange.com/questions/11192/what-lisp-compilers-and-interpreters-were-available-for-8-bit-machines)

## LLVM

* [Kaleidoscope: Kaleidoscope Introduction and the Lexer](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html)
* [A Julia wrapper for the LLVM C API.](https://github.com/maleadt/LLVM.jl/blob/master/README.md)

### Lisp and Scheme

* [(How to Write a (Lisp) Interpreter (in Python))](http://www.norvig.com/lispy.html)
* [(An ((Even Better) Lisp) Interpreter (in Python))](http://norvig.com/lispy2.html)
* [beau­tiful racket -an intro­duc­tion to language-orientedprogramming](https://beautifulracket.com/)
* [Bits of information about Lisp, Scheme, 8 bit LISP](http://web.archive.org/web/20100131151915/http://www.ip9.org/munro/skimp/)
* [The Make-A-Lisp Process](https://github.com/kanaka/mal/blob/master/process/guide.md)
* [uLisp](http://www.ulisp.com/show?1AA0)
* [micro-lisp](https://github.com/carld/micro-lisp)
* [femtolisp - a lightweight, robust, scheme-like lisp implementation used in julia](https://github.com/JeffBezanson/femtolisp)
* [LISP on the BBC Microcomputer Remastered PDF](https://stardot.org.uk/forums/viewtopic.php?t=17811)
## Middle

## Back Ends

* Someone wrote a Lisp assembler for the 6502 and wrote a blog about it. [Fun with Lisp: Programming the NES](https:/ahefner.livejournal.com/20528.html) with [code on github](https://github.com/ahefner/asm6502)
* [LISP/8-6502 interpreter](http://web.archive.org/web/20090106184314/http://www.hugbox.org/lisp8/lisp-6502.asm)
* [6502 “Illegal” Opcodes Demystified](https://www.masswerk.at/nowgobang/2021/6502-illegal-opcodes)
* [Henry Baker's COMFY compiler for the 6502 processor
ported to Common Lisp](https://github.com/jaoswald/cl-comfy-6502)
* [Lisp interpreter written for the Apple //e.](https://github.com/hausdorff/turtles)
* [Implementing Lisp for 6502/65C816](http://forum.6502.org/viewtopic.php?t=1427)
* [David A. Wheeler's 6502 Language Implementation Approaches](https://dwheeler.com/6502/)
* Readable [MAE Manual](https://atariwiki.org/wiki/attach/MAE%20Assembler/MAE_Manual.pdf)
* [EHS Disk Macro Assembler/Text Editor (MAE) - Manual](https://archive.org/details/EHSDiskMacroAssemblerManual/mode/2up)
* [PDP-11 Lisp implementation](http://archive.computerhistory.org/resources/text/DEC/pdp-1/DEC.pdp_1.1964.102650371.pdf)

### C64 Specific

* [The Transactor Online Archive](ttp://csbruce.com/cbm/transactor/) and [Disks](http://csbruce.com/cbm/transactor/disks/)
* [Craig's 8-bit Commodore Page](http://csbruce.com/cbm/)
* [Transactor article that discusses Lisp on C64 - suggests and additiona disk on Page 41 with a special MAE Assembler source to Micro-Lisp](http://csbruce.com/cbm/transactor/pdfs/trans_v8_i06.pdf)
* [Just the Micro-Lisp article](https://www.lyonlabs.org/commodore/onrequest/micro-lisp.pdf)
* ["Micro-Lisp" a lisp for the C64](https://groups.google.com/g/comp.lang.lisp/c/6pPNzzpVV9o) attach the image, `LOAD"MICRO-LISP",8,1` then `RUN` 
* [Versatile Commodore Emulator](https://vice-emu.sourceforge.io/windows.html)
Keyboard is a bit weird. "Go into the WinVICE directory, then into the C64 directory. Looks for the file win_pos.vkm. Rename it to win_pos.vkm.bak then copy the win_pos.vkm from the link above into the C64 directory. You should then be able to use the keyboard (mostly) normally. The Tab key still acts as the CTRL key on the C64, and the left CTRL key acts as the C= key." File has disappeared. But this is the [forum link](https://www.lemon64.com/forum/viewtopic.php?t=40321)
* [How do I run .T64 and .D64 files in an emulator](https://www.lemon64.com/forum/viewtopic.php?t=40321) For D64, you you need File -> Attach disk image -> Drive 8, and then most likely type LOAD"*",8,1 to load the first program on the disk.
* [How do I get a list of files on a floppy disk in C64 BASIC?](https://www.lemon64.com/forum/viewtopic.php?t=27891#:~:text=Enter%20the%20following%3A%20LOAD%22%24%22%2C8%20Then%20press%20return.%20The,What%20you%20see%20is%20what%27s%20on%20the%20disk.) - attach the disk on the emulator (say 8) `LOAD"$",8` and then `LIST` to see the files.
* [The Codebase: Sourcecode, Articles & Tutorials](http://codebase64.org/doku.php?id=base:start)
* [Code for the C64 - reading the directory](http://codebase64.org/doku.php?id=base:reading_the_directory)
* [Assembly](https://en.wikibooks.org/wiki/6502_Assembly)

http://telarity.com/~dan/cbm/languages.html
Weird archive formats: possibly 16 bit operating systems.

Nicholas Vrtis, Transactor Publishing Inc., Vol.8,Iss.6)
LISP interpreter. All numbers are stored as 24 bit integers.
<http://www.csbruce.com/cbm/ftp/c64/programming/mlisp1p2.arc>
<https://www.funet.fi/pub/cbm/c64/programming/mlisp.sfx>

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
* [Example](https://example.com)
