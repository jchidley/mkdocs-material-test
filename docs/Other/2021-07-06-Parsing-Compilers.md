---
date: "2021-07-06"
title: "Parsing and Compilers"
tags:
  - compilers
  - parsing
  - programming-languages
---
<!-- markdownlint-disable MD025 -->
# Parsing Compilers
<!-- markdownlint-enable MD025 -->

!!! info "Related Articles"
    For front-end parsing libraries (Rust, Julia), Lisp/Scheme implementations, back-ends (6502, QBE), and emulation resources, see [Writing A Programming Language](../2023-09-04-Writing-A-Programming-Language.md).

[mold - a new linker](https://github.com/rui314/mold) [mold - a modern linker](https://youtu.be/hAt3kCalE0Y?si=71Ezpd2wGznau_IH)

Faster programs:
* don't guess, measure
* Data is usually way more important than code: better data structures are key
* Try several algorithms and pick the fasted (measure!)
* Write the same program several times

## Compiler Information

Some books are:
* I bought, and downloaded `Crafting Interpreters.pdf`, [Crafting Interpreters](https://craftinginterpreters.com/)
* [Crafting Interpreters reference books](https://twitter.com/munificentbob/status/901543375945388032)
* Lisp in small pieces by Christian Queinnec 978-0521545662
* Crafting a compiler by Charles N Fischer 978-0805332018
* A retargetable C compiler by Christopher W. Fraser 978-0805316704
* Build Your Own Lisp by Daniel Holden 978-1501006623

* This is easily the best reference: [CSE 401 Spring 2023 Lectures](https://courses.cs.washington.edu/courses/cse401/23sp/calendar/lecturelist.html)
* Best YouTube: [compiler_series: Material for the Creating a Compiler video lesson series.](https://github.com/bisqwit/compiler_series)
* Practical, step-by-step, compiler [chibicc: A small C compiler](https://github.com/rui314/chibicc) and [chibicc documentation, in Japanese](https://www.sigbus.info/compilerbook)
* [Crafting Interpreters](https://craftinginterpreters.com) and [Crafting "Crafting Interpreters"](https://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/)
* System, compiler, RISC, FPGA, the whole lot [Niklaus Wirth](https://people.inf.ethz.ch/wirth/) and [Project Oberon](http://www.projectoberon.net) with an [Open Core](https://opencores.org/projects/oberon_sdram) and a [risc-v version](https://github.com/solbjorg/oberon-riscv)
* [minilisp: A readable lisp in less than 1k lines of C](https://github.com/rui314/minilisp/tree/master) and a version for ULX3S [GitHub - emard/oberon](https://github.com/emard/oberon)
* Make a Lisp [mal - Make a Lisp](https://github.com/kanaka/mal)
* [Show HN: How to write a tiny compiler | Hacker News](https://news.ycombinator.com/item?id=13608810)
* [Recommendations](https://belkadan.com/blog/2015/11/Recommendations/) and [So You Want to Be a (Compiler) Wizard?](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/)
* [Compiler Construction](https://people.inf.ethz.ch/wirth/CompilerConstruction/index.html) with [Chapters 1-8](https://people.inf.ethz.ch/wirth/CompilerConstruction/CompilerConstruction1.pdf) and [Chapters 9-16](https://people.inf.ethz.ch/wirth/CompilerConstruction/CompilerConstruction2.pdf)
* [Let's write a compiler, part 1: Introduction, selecting a language, and doing some planning](https://briancallahan.net/blog/20210814.html)
* [GitHub - rswier/c4: C in four functions](https://github.com/rswier/c4)
* [1 What is a Compiler?](https://www.cs.umd.edu/class/fall2020/cmsc430/Intro.html)
* [An Incremental Approach to Compiler Construction](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf)
* [cproc is a C11 compiler using QBE as a backend](https://git.sr.ht/~mcf/cproc)
* [Let's get hands-on with QBE](https://briancallahan.net/blog/20210829.html)
* [The ppci (pure python compiler infrastructure) project is a compiler written entirely in python](https://ppci.readthedocs.io/en/latest/index.html) with [Creating a toy language -- ppci 0.5.9 documentation](https://ppci.readthedocs.io/en/latest/howto/toy.html)
* [C to Assembly Translation](https://www.eventhelix.com/embedded/c-to-assembly-translation/)
* [A Guide to Code Generation - Strumenta](https://tomassetti.me/code-generation/)
* [Compiler/code generator - Rosetta Code](https://rosettacode.org/wiki/Compiler/code_generator#Python)
* [Introduction to Compilers and Language Design](https://www3.nd.edu/~dthain/compilerbook/) 
* [Lecture 26, Code Generation](https://homepage.cs.uiowa.edu/~dwjones/compiler/notes/26.shtml)
* [Building a Compiler with MLIR](https://llvm.org/devmtg/2020-09/slides/MLIR_Tutorial.pdf)
* [Code Generation for Data Processing - Chair for Database Systems](https://db.in.tum.de/teaching/ws2223/codegen/index.shtml?lang=en)
* [Target Code Generation](https://courses.cs.washington.edu/courses/cse401/07au/CSE401-07cogen.pdf)
* site:https://courses.cs.washington.edu intermediate code generation
* [CSE401: Introduction to Compiler Construction](https://courses.cs.washington.edu/courses/cse401/)
* [Compiler Optimization and Code Generation](https://bears.ece.ucsb.edu/class/ece253/compiler_opt/c2.pdf)
* [6.035: Computer Language Engineering](http://cons.mit.edu/sp13/schedule.html)
* [Code-generator generators: generating the instruction selector](https://www.lrde.epita.fr/dload/20040602-Seminar/vasseur0604_code-gen-gen_report.pdf)
* [The lcc retargetable ANSI C compiler](https://github.com/drh/lcc)
* [Small-C Compiler](https://github.com/ncb85/SmallC-85) with [Developer Network Small-C Compiler book on CD-ROM | Dr Dobb’s](https://www.drdobbs.com/developer-network-small-c-compiler-book/184415519?queryText=%2522small%2Bc%2522) - includes K&R writing and [Small-C - Wikipedia](https://en.wikipedia.org/wiki/Small-C)

```shell
jackc@LAPTOP-VNSPU3KP:/mnt/c/Users/jackc/Downloads$ sudo mount -o loop ddj_devnetwork_small_c.iso /mnt/iso/
\\wsl.localhost\U3\mnt\iso
```

```C
#include <stdio.h>

int main(void)
{
  printf("Hello World\n");
  return 0;
}
```

## Compiler Tools

* [User manual (C) -- re2c 3.0 documentation](https://re2c.org/manual/manual_c.html)
*  [Flex, A fast scanner generator](https://www.cs.princeton.edu/~appel/modern/c/software/flex/flex.html)
* [GNU Bison - The Yacc-compatible Parser Generator - GNU Project - Free Software Foundation](https://www.gnu.org/software/bison/manual/)
* [GNU make](https://www.gnu.org/software/make/manual/make.html#Wildcard-Examples)
* [Makefile Tutorial](https://makefiletutorial.com/#getting-started)

## Links

* [Whirlwind Tour of ARM Assembly](http://www.coranac.com/tonc/text/asm.htm)
* [ARM Assembler](http://www.pp4s.co.uk/main/tu-trans-asm-arm.html)
* [PP4S: Introduction](http://www.pp4s.co.uk/main/tu-trans-comp-jc-01.html)
* [Let’s Build a Compiler, by Jack Crenshaw](https://compilers.iecc.com/crenshaw/)
* [Writing a C Compiler, Part 1](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
* [Raspberry Pi Pico, VSCode and MacOS](https://www.chrisclaxton.me.uk/chris-claxtons-blog/raspberry-pi-pico-vscode-and-macos)
* [Stephen Smith's Blog - Musings on Machine Learning… - Posts Tagged ‘assembly language’](https://smist08.wordpress.com/tag/assembly-language/)
* [1. ASM Programming RP2040 - Assembly Language on the Raspberry Pi Pico](https://smist08.wordpress.com/2021/04/16/assembly-language-on-the-raspberry-pi-pico/)
* [2. ASM Programming RP2040 - Calling Main in Assembly Language on the RP2040](https://smist08.wordpress.com/2021/04/23/calling-main-in-assembly-language-on-the-rp2040/)
* [3. ASM Programming RP2040 - Bit-Banging the Raspberry Pi Pico’s GPIO Registers](https://smist08.wordpress.com/2021/04/24/bit-banging-the-raspberry-pi-picos-gpio-registers/)
* [How to Use Inline Assembly Language in C Code](https://gcc.gnu.org/onlinedocs/gcc/Using-Assembly-Language-with-C.html)
* [Compiling a Lisp: Overture](https://bernsteinbear.com/blog/compiling-a-lisp-0/)
* [Programming languages resources](https://bernsteinbear.com/pl-resources/)
* [textX](http://textx.github.io/textX/stable/)
* [Arpeggio](https://textx.github.io/Arpeggio/stable/)
* [Overview — MicroPython 1.16 documentation](https://docs.micropython.org/en/latest/index.html)
* [inc: an incremental approach to compiler construction](https://github.com/namin/inc)

* [ARM® and Thumb®-2 Instruction Set Quick Reference Card](https://documentation-service.arm.com/static/5ed66080ca06a95ce53f932d?token=)
* [Parsing/RPN calculator algorithm - Rosetta Code](https://rosettacode.org/wiki/Parsing/RPN_calculator_algorithm#Python)
* [A RPN Calculator in F# Stefano Ricciardi](http://www.stefanoricciardi.com/2010/10/01/a-rpn-calculator-in-f/)
* [Additional Reading](https://cseweb.ucsd.edu/classes/sp17/cse131-a/s_materials.html)

* [C++ Core Guidelines](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-introduction)

* [26 programming languages in 25 days, Part 2: Reflections on language design](https://matt.might.net/articles/26-languages-part2/)
* [Day 1 - Advent of Code 2022](https://adventofcode.com/2022/day/1)

* [Running Bare Metal Applications on QEMU](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/821854273/Running+Bare+Metal+Applications+on+QEMU)

* [femtolisp is a simple, elegant Scheme dialect](https://github.com/JeffBezanson/femtolisp)

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
