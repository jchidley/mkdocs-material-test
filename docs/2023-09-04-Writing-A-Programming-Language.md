---
date: "2023-09-04"
title: "Writing-A-Programming-Language"
---
<!-- markdownlint-disable MD025 -->
# Writing A Programming Language
<!-- markdownlint-enable MD025 -->

[The idea behind single-header file libraries](https://github.com/nothings/stb)

## Introduction

What language to learn?

* Leading indicator [PYPL PopularitY of Programming Language](https://pypl.github.io/PYPL.html)
* Lagging indicator [The RedMonk Programming Language Rankings: June 2024](https://redmonk.com/sogrady/2024/09/12/language-rankings-6-24/)
* One person's perspective [26 programming languages in 25 days, Part 2: Reflections on language design](https://matt.might.net/articles/26-languages-part2/)

* [How to Design Programs, Second Edition](https://htdp.org/2023-8-14/Book/index.html)
* [LET'S BUILD A COMPILER! By Jack W. Crenshaw, Ph.D.](https://compilers.iecc.com/crenshaw/tutor1.txt)
* [The ppci (pure python compiler infrastructure) project is a compiler written entirely in python](https://ppci.readthedocs.io/en/latest/index.html)
* [an incremental approach to compiler construction](https://github.com/namin/inc)
* [Additional Reading](https://cseweb.ucsd.edu/classes/sp17/cse131-a/s_materials.html)
* Lots or articles including parsing, compiling [Matt Might's blog](https://matt.might.net/articles/)
* [Compiler Explorer](https://godbolt.org) and [Matt Godbolt’s blog](https://xania.org)
* [8bitworkshop](https://8bitworkshop.com)

## Front Ends

* [What LISP compilers and interpreters were available for 8-bit machines?](https://retrocomputing.stackexchange.com/questions/11192/what-lisp-compilers-and-interpreters-were-available-for-8-bit-machines)
* [Modular Docs - Mojo🔥](https://docs.modular.com/mojo/?utm_medium=email&_hsmi=256256127&_hsenc=p2ANqtz--3cgzgmX_1b1E5s1WK7OZiWeLuQ59ylpa7KSCo85ycrmVYf2yZqvzHwwUC6EFHh_l0TjtgzrhMrePktSNQG6UKtNtbxw&utm_content=256256127&utm_source=hs_automation)
* [Getting Started - MLIR](https://mlir.llvm.org/getting_started/)

### Parsing

Here's a few introductory texts: 

* [When to use a Parser Combinator? When to use a Parser Generator?](https://softwareengineering.stackexchange.com/questions/338665/when-to-use-a-parser-combinator-when-to-use-a-parser-generator)
* [LL and LR in Context: Why Parsing Tools Are Hard](https://blog.reverberate.org/2013/09/ll-and-lr-in-context-why-parsing-tools.html)
* [LL and LR Parsing Demystified](https://blog.reverberate.org/2013/07/ll-and-lr-parsing-demystified.html)

* [fparsec Tutorial](https://www.quanttec.com/fparsec/tutorial.html)
* [Lerche (German for Lark) is a partial port of the Lark grammar processor from Python to Julia](https://github.com/jamesrhester/Lerche.jl)
* [Lark - a parsing toolkit for Python](https://github.com/lark-parser/lark)
* [Automa is a regex-to-Julia compiler.](https://biojulia.dev/Automa.jl/previews/PR119/)
* [CombinedParsers in pure Julia](https://github.com/gkappler/CombinedParsers.jl)
* [Rex Eats Regular Expressions for Breakfast](https://www.rexegg.com/)

* [AbstractTrees.jl](https://juliacollections.github.io/AbstractTrees.jl/stable/)
* [Trees in Julia](https://discourse.julialang.org/t/trees-in-julia/12173)
* [GraphMakie.jl In this example we are going to plot an abstract syntax tree of a Julia function using the Bucheim Layout from NetworkLayout.jl.](https://graph.makie.org/dev/generated/syntaxtree/)

#### Rust

* [winnow aims to be your “do everything” parser, much like people treat regular expressions.](https://docs.rs/winnow/latest/winnow/)
* [nom - A byte-oriented, zero-copy, parser combinators library](https://lib.rs/crates/nom), [The Nom Guide (Nominomicon)](https://tfpk.github.io/nominomicon/)
* [lalrpop - convenient LR(1) parser generator](https://lib.rs/crates/lalrpop), [LALRPOP Book](https://lalrpop.github.io/lalrpop/)
* [logos - Create ridiculously fast Lexers](https://lib.rs/crates/lalrpop), [Logos Handbook](https://logos.maciej.codes/)
* [combine - Fast parser combinators on arbitrary streams with zero-copy support](https://lib.rs/crates/combine), [combine wiki](https://github.com/Marwes/combine/wiki)
* [pest - The Elegant Parser](https://lib.rs/crates/pest), [pest book](https://pest.rs/book/)

### LLVM

* [llvm-mos](https://llvm-mos.org/wiki/Welcome)
* [Kaleidoscope: Kaleidoscope Introduction and the Lexer](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html)
* [A Julia wrapper for the LLVM C API.](https://github.com/maleadt/LLVM.jl/blob/master/README.md)

### C

* Practical, step-by-step, compiler [chibicc: A small C compiler](https://github.com/rui314/chibicc) and [chibicc documentation, in Japanese](https://www.sigbus.info/compilerbook)
* [cproc: Small C11 compiler based on QBE](https://sr.ht/~mcf/cproc/)

### Lisp and Scheme

* [On Lisp is a comprehensive study of advanced Lisp techniques](https://www.lurklurk.org/onlisp/onlisp.html)
* [(How to Write a (Lisp) Interpreter (in Python))](http://www.norvig.com/lispy.html)
* [(An ((Even Better) Lisp) Interpreter (in Python))](http://norvig.com/lispy2.html)
* [Learning with Peter Norvig's lis.py interpreter](https://github.com/fluentpython/lispy)
* Lots more information and links [Scheme (programming language) - Wikipedia](https://en.wikipedia.org/wiki/Scheme_(programming_language))
* [beau­tiful racket - an intro­duc­tion to language-oriented programming](https://beautifulracket.com/)
* [Racket Documentation](https://docs.racket-lang.org/)
* [Bits of information about Lisp, Scheme, 8 bit LISP](http://web.archive.org/web/20100131151915/http://www.ip9.org/munro/skimp/)
* [The Make-A-Lisp Process](https://github.com/kanaka/mal/blob/master/process/guide.md)
* [uLisp](http://www.ulisp.com/show?1AA0)
* [micro-lisp](https://github.com/carld/micro-lisp)
* [femtolisp - a lightweight, robust, scheme-like lisp implementation used in julia](https://github.com/JeffBezanson/femtolisp)
* [LISP on the BBC Microcomputer Remastered PDF](https://stardot.org.uk/forums/viewtopic.php?t=17811)

## Middle

* [Mapping Python to LLVM | Exaloop blog](https://blog.exaloop.io/python-llvm/)
* [A guide that explains how high level programming language constructs are mapped to the LLVM intermediate language.](https://github.com/f0rki/mapping-high-level-constructs-to-llvm-ir)
* [Netwide Assembler (NASM), an asssembler for the x86 CPU architecture portable to nearly every modern platform, and with code generation for many platforms old and new.](https://www.nasm.us/index.php)
* [vbcc Compiler System](http://www.ibaug.de/vbcc/doc/vbcc.pdf)

## Back Ends

* [Code Generation](https://fileadmin.cs.lth.se/cs/Education/EDAN65/2021/lectures/L11.pdf)
* Someone wrote a Lisp assembler for the 6502 and wrote a blog about it. [Fun with Lisp: Programming the NES](https:/ahefner.livejournal.com/20528.html) with [code on github](https://github.com/ahefner/asm6502)
* [QBE - Compiler Backend](https://c9x.me/compile/)
* [Let's get hands-on with QBE](https://briancallahan.net/blog/20210829.html)
* [LISP/8-6502 interpreter](http://web.archive.org/web/20090106184314/http://www.hugbox.org/lisp8/lisp-6502.asm)
* [6502 “Illegal” Opcodes Demystified](https://www.masswerk.at/nowgobang/2021/6502-illegal-opcodes)
* [Henry Baker's COMFY compiler for the 6502 processor ported to Common Lisp](https://github.com/jaoswald/cl-comfy-6502)
* [Lisp interpreter written for the Apple //e.](https://github.com/hausdorff/turtles)
* [Implementing Lisp for 6502/65C816](http://forum.6502.org/viewtopic.php?t=1427)
* [David A. Wheeler's 6502 Language Implementation Approaches](https://dwheeler.com/6502/)
* Readable [MAE Manual](https://atariwiki.org/wiki/attach/MAE%20Assembler/MAE_Manual.pdf)
* [EHS Disk Macro Assembler/Text Editor (MAE) - Manual](https://archive.org/details/EHSDiskMacroAssemblerManual/mode/2up)
* [PDP-11 Lisp implementation](http://archive.computerhistory.org/resources/text/DEC/pdp-1/DEC.pdp_1.1964.102650371.pdf)

### Linker

* [Beginner's Guide to Linkers](https://www.lurklurk.org/linkers/linkers.html)
* [mold: A Modern Linker](https://github.com/rui314/mold)

### C64 Specific

* [The Transactor Online Archive](ttp://csbruce.com/cbm/transactor/) and [Disks](http://csbruce.com/cbm/transactor/disks/)
* [Craig's 8-bit Commodore Page](http://csbruce.com/cbm/)
* [Transactor article that discusses Lisp on C64 - suggests and additiona disk on Page 41 with a special MAE Assembler source to Micro-Lisp](http://csbruce.com/cbm/transactor/pdfs/trans_v8_i06.pdf)
* [Just the Micro-Lisp article](https://www.lyonlabs.org/commodore/onrequest/micro-lisp.pdf)
* ["Micro-Lisp" a lisp for the C64](https://groups.google.com/g/comp.lang.lisp/c/6pPNzzpVV9o) attach the image, `LOAD"MICRO-LISP",8,1` then `RUN`
* [Versatile Commodore Emulator](https://vice-emu.sourceforge.io/windows.html)
Keyboard is a bit weird: Tab key acts as the CTRL key on the C64, and the left CTRL key acts as the C= key. Replacing `win_pos.vkm` file in the WinVICE/C64 directory with a new keymap. [forum link](https://www.lemon64.com/forum/viewtopic.php?t=40321)
* [How do I run .T64 and .D64 files in an emulator](https://www.lemon64.com/forum/viewtopic.php?t=40321) For D64, you you need File -> Attach disk image -> Drive 8, and then most likely type LOAD"*",8,1 to load the first program on the disk.
* [How do I get a list of files on a floppy disk in C64 BASIC?](https://www.lemon64.com/forum/viewtopic.php?t=27891#:~:text=Enter%20the%20following%3A%20LOAD%22%24%22%2C8%20Then%20press%20return.%20The,What%20you%20see%20is%20what%27s%20on%20the%20disk.) - attach the disk on the emulator (say 8) `LOAD"$",8` and then `LIST` to see the files.
* [The Codebase: Sourcecode, Articles & Tutorials](http://codebase64.org/doku.php?id=base:start)
* [Code for the C64 - reading the directory](http://codebase64.org/doku.php?id=base:reading_the_directory)
* [Assembly](https://en.wikibooks.org/wiki/6502_Assembly)

### 6502 Emulation / Builds

* [A 6502 emulator in Lisp](https://github.com/kingcons/cl-6502)
* [Obelisk Home Pages](http://www.6502.org/users/obelisk/)
* [Reverse Engineering the MOS 6502 CPU](https://media.ccc.de/v/27c3-4159-en-reverse_engineering_mos_6502)
* [Bario.2001.emubook Study of the techniques for emulation programming](http://www.xsim.com/papers/Bario.2001.emubook.pdf)
* [Emulate 6502-based microcomputer systems in Python](https://github.com/mnaberez/py65)
* [lib6502 6502 in C](https://www.piumarta.com/software/lib6502/)
* [an Apple // emulator in Python](https://github.com/jtauber/applepy) and [YouTube](https://youtu.be/EhK5JNx0irA?si=QYigx5cVZHbBJqa-)
* [Emulating a BBC Micro in Javascript — Matt Godbolt’s blog](https://xania.org/201405/jsbeeb-emulating-a-bbc-micro-in-javascript)
* [virtual 6502 Emulator](https://www.masswerk.at/6502/)
* YouTube [Emulating a CPU in C++ (6502)](https://www.youtube.com/watch?v=qJgsuQoy9bc) and GitHub [Learning how a CPU works by emulating one](https://github.com/davepoo/6502Emulator)
* [8bitworkshop IDE](https://8bitworkshop.com/v3.10.1/?platform=c64&file=hello.dasm#)
* [](https://8bitworkshop.com/v3.10.1/?platform=c64&file=hello.dasm)
* [dasm](https://dasm-assembler.github.io/)
* [Writing a 6502 emulator in Python](https://dailystuff.nl/projects/writing-a-6502-emulator-in-python) and [6502 emulator in Python](https://github.com/hspaans/python-6502-emulator#introduction)
* [A fast & simple MOS 6502 CPU emulator written in C++](https://github.com/gianlucag/mos6502)
* [Easy 6502 by skilldrick](https://skilldrick.github.io/easy6502/)
* [Code for the 6502 microprocessor, mostly for the Replica 1 computer.](https://github.com/jefftranter/6502/tree/master)
* [RetroVGA - Raspbery Pico multi retro computer from Bobricius on Tindie](https://www.tindie.com/products/bobricius/retrovga-raspbery-pico-multi-retro-computer/)
* This is a collection of emulators [M.CU.M.E = Multi CompUter Machine Emulator](https://github.com/Jean-MarcHarvengt/MCUME/tree/master/MCUME_pico/bin/PICOMPUTERMAX)
* Lots of references and hardware [ZX Spectrum for Raspberry Pico Pi RP2040](https://github.com/fruit-bat/pico-zxspectrum)

<!-- markdownlint-disable MD034 -->
http://telarity.com/~dan/cbm/languages.html
<!-- markdownlint-enable MD034 -->
Weird archive formats: possibly 16 bit operating systems.

Nicholas Vrtis, Transactor Publishing Inc., Vol.8,Iss.6)
LISP interpreter. All numbers are stored as 24 bit integers.
<http://www.csbruce.com/cbm/ftp/c64/programming/mlisp1p2.arc>
<https://www.funet.fi/pub/cbm/c64/programming/mlisp.sfx>

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
* [Example](https://example.com)
