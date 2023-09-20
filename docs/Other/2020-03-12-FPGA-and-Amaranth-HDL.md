---
date: "2020-03-12"
title: "FPGA-and-Amaranth-HDL"
---
<!-- 2020-03-12-Toolchain.md -->

<!-- markdownlint-disable MD025 -->
# FPGA and Amaranth HDL
<!-- markdownlint-enable MD025 -->

## Introduction

https://web.mit.edu/6.111/www/f2017/handouts/TheDigitalWorld.pdf

* [GitHub - amaranth-lang/amaranth: A modern hardware definition language and toolchain based on Python](https://github.com/amaranth-lang/amaranth)
* [Snippet from a talk about LUNA](https://talks.toorcon.net/media/toorcon-2021/question_uploads/Unauthorized_Guide_to_LUNA_xK3u1SN.pptx)
Basic building block extends elaboratable
•elaborate method returns a Module to synthesize
•Elaboratables have ports (public attributes)
•Modules have submodules
•Modules have multiple domains:
•comb: simple combinatorial logic (asynchronous)
•Clock-synchronous domains
Default is called sync and is automatically connected to the primary platform clock

* [Including non-nMigen Instances in nMigen - kate's lab notebook](https://lab.ktemkin.com/post/nmigen-instance/)
* [amaranth | Open Research Institute](https://www.openresearch.institute/tag/amaranth/) with https://github.com/maia-sdr/maia-sdr/tree/main/maia-hdl
* [Amaranth-HDL built movement engine](https://github.com/hstarmans/hexastorm/blob/master/src/hexastorm/movement.py)
* [hexastorm](https://github.com/hstarmans/hexastorm/tree/master) [based on this paper](http://www.roboticsproceedings.org/rss10/p42.pdf)
* [More Amaranth HDL stuff with `*.v` files too](https://github.com/sensille/conan_fpga/blob/master/movequeue.py)
* [fpga4fun.com - where FPGAs are fun](https://www.fpga4fun.com)
* [Language & toolchain — Amaranth HDL toolchain 0.4.dev197 documentation](https://amaranth-lang.org/docs/amaranth/latest/index.html)
* [Learning FPGA Design with nMigen – Vivonomicon's Blog](https://vivonomicon.com/2020/04/14/learning-fpga-design-with-nmigen/)
* [Let’s Write a Minimal RISC-V CPU in nMigen – Vivonomicon's Blog](https://vivonomicon.com/2020/06/13/lets-write-a-minimal-risc-v-cpu-in-nmigen/)
* [Learning how to FPGA with ‘Neopixel’ LEDs – Vivonomicon's Blog](https://vivonomicon.com/2018/12/24/learning-how-to-fpga-with-neopixel-leds/)
* [GitHub - jonnew/learn-migen: migen tutorials, etc](https://github.com/jonnew/learn-migen/tree/master)
* [nMigen for 6800 CPU development](https://www.youtube.com/watch?v=AQOXoKQhG3I&list=PL2Bqmy_B2P9t8sFYz39OC9eWEAke7E3nt&index=30)
* [Introduction — LUNA documentation](https://luna.readthedocs.io/en/latest/intro.html)
* [Including non-Amaranth Instances in Amaranth - kate's lab notebook](https://lab.ktemkin.com/post/amaranth-instance/)
* [GitHub - greatscottgadgets/luna: a USB multitool + Amaranth HDL framework for monitoring, hacking, and developing USB devices](https://github.com/greatscottgadgets/luna)
* [Exploring Open-Toolchain FPGA HW, part 1](https://www.ktemkin.com/exploring-open-fpga-hardware/)
* [Cynthion - Great Scott Gadgets](https://greatscottgadgets.com/cynthion/)
* [SymbiFlow Getting Started](https://symbiflow.readthedocs.io/en/latest/symbiflow-arch-defs/docs/source/getting-started.html)

Get yosys from [here](http://www.clifford.at/yosys/download.html)
Install in P:\Tools\yosys-win32-mxebin-0.9 and add that to the user's PATH environment variable

* [Open Source FPGA tool flow part 1: yosys](https://www.youtube.com/watch?v=A5AHglpfdtQ&list=PL2Bqmy_B2P9t8sFYz39OC9eWEAke7E3nt&index=12)
* [Catherine @whitequark - developer of Amaranth HDL](https://cohost.org/whitequark)
* [#nmigen on 2020-07-31 — irc logs at freenode.irclog.whitequark.org](https://freenode.irclog.whitequark.org/nmigen/2020-07-31)

### HDLs

* [Silice is an open source language that simplifies prototyping and writing algorithms on FPGA architectures.](https://github.com/sylefeb/Silice/tree/master)
* [SpinalHDL · GitHub](https://github.com/SpinalHDL)
* [Demo - Litex Development Enviroment - Public Docs - Trenz Electronic Wiki](https://wiki.trenz-electronic.de/display/PD/Demo+-+Litex+Development+Enviroment)

### Tutorials, Examples

* [FPGA-101: Introduction to FPGAs, Learn the Basics](https://nandland.com/fpga-101/)
* [Getting Started with FPGAs | No Starch Press](https://nostarch.com/gettingstartedwithfpgas)
* [How I went from blinker to RSIC-V in 3 months](https://blog.yosyshq.com/p/blinker-to-risc-v/)
* [Introductory Digital Systems Laboratory](https://web.mit.edu/6.111/www/f2016/)
* [Building FPGA Gateware with Verilog and Amaranth: A Tutorial — CFU-Playground documentation](https://cfu-playground.readthedocs.io/en/latest/crash-course/gateware.html#part-2-amaranth-basics)
* [learning nmigen](https://libre-soc.org/docs/learning_nmigen/)
* [Stuff about luna and nmigen / amaranth](https://talks.toorcon.net/media/toorcon-2021/question_uploads/Unauthorized_Guide_to_LUNA_xK3u1SN.pptx)
* [HDL workflow](https://libre-soc.org/HDL_workflow/)
* [fpgacpu.org - FPGA CPU News](http://www.fpgacpu.org/index.html)
* [assembly - Implementation of simple microprocessor using verilog - Stack Overflow](https://stackoverflow.com/questions/51592244/implementation-of-simple-microprocessor-using-verilog/51621153#51621153)
* [bl0x/learn-fpga-amaranth: Code for Bruno Levy's learn-fpga tutorial written in Amaranth HDL](https://github.com/bl0x/learn-fpga-amaranth/tree/main)
* [GitHub - BrunoLevy/learn-fpga: Learning FPGA, yosys, nextpnr, and RISC-V](https://github.com/BrunoLevy/learn-fpga/tree/master)
* [Yosys Headquarters · GitHub](https://github.com/YosysHQ)
* [YosysHQ Documentation Library](https://yosyshq.readthedocs.io/en/latest/index.html#yosyshq-documentation-library)
* [oss-cad-suite-build: Multi-platform nightly builds of open source digital design and verification tools](https://github.com/YosysHQ/oss-cad-suite-build)
* [Implementing a simple SoC in Migen — whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-19/implementing-a-simple-soc-in-migen/)
* [Circuit Simulator Applet](http://falstad.com/circuit/)
* [FPGA Bootcamp #0 | Hackaday.io](https://hackaday.io/project/159720-fpga-bootcamp-0)
*  [Implementing a UART in Verilog and Migen — whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-18/implementing-an-uart-in-verilog-and-migen/)
* [GitHub - kbob/nmigen-examples: I want to learn nMigen](https://github.com/kbob/nmigen-examples/tree/master)
* [GitHub - RobertBaruch/nmigen-tutorial: A tutorial for using nmigen](https://github.com/RobertBaruch/nmigen-tutorial)
* [Designing a RISC-V CPU, Part 1: Learning hardware design as a software engineer](https://mcla.ug/blog/risc-v-cpu-part-1.html)
* [migen:tutorial](https://web.archive.org/web/20180813074637/http://blog.lambdaconcept.com/doku.php?id=migen:tutorial)
* [Including non-Amaranth Instances in Amaranth - kate's lab notebook](https://lab.ktemkin.com/post/amaranth-instance/)
* [learning nmigen](https://libre-soc.org/docs/learning_nmigen/)
* [Libre-soc-dev nmigen tutorials etc.](http://lists.libre-soc.org/pipermail/libre-soc-dev/2021-October/003858.html)
* [ULX3S nMigen examples](https://github.com/GuzTech/ulx3s-nmigen-examples/blob/master/README.md)
* [iCEBreaker amaranth examples](https://github.com/icebreaker-fpga/icebreaker-amaranth-examples/blob/master/README.md)
* [fpga4fun.com - where FPGAs are fun](https://www.fpga4fun.com)
* [litex FPGA 101 lessons/labs](https://github.com/litex-hub/fpga_101/tree/master)
* [GitHub - osresearch/up5k: Upduino v2 with the ice40 up5k FPGA demos](https://github.com/osresearch/up5k)
* [🎲 A Tiny and Platform-Independent True Random Number Generator for any FPGA.](https://github.com/stnolting/neoTRNG)
* [learn-fpga: Learning FPGA, yosys, nextpnr, and RISC-V](https://github.com/BrunoLevy/learn-fpga)
* [Building risc on FPGA](http://www.fpgacpu.org/papers/xsoc-series-drafts.pdf)

#### old but useful

* [Porting a New Board To Migen](https://www.wdj-consulting.com/blog/migen-port/)
* [Migen Tutorial](https://m-labs.hk/docs/migen-tutorial.pdf)
* [Migen manual — Migen 0.8.dev0 documentation](https://m-labs.hk/migen/manual/)
* [Migen | M-Labs](https://m-labs.hk/gateware/migen/)

probably worth looking up Migen documentation

### Hardware

* [UPduino Documentation — UPduino 0.1 documentation](https://upduino.readthedocs.io/en/latest/index.html)
* [ULX3S | Crowd Supply](https://www.crowdsupply.com/radiona/ulx3s)
* [GitHub - devantech/iceFUN](https://github.com/devantech/iceFUN)

### Risc-V

* [The NEORV32 RISC-V Processor](https://stnolting.github.io/neorv32/)
* [GitHub - SpinalHDL/VexRiscv: A FPGA friendly 32 bit RISC-V CPU implementation](https://github.com/SpinalHDL/VexRiscv)
* [Ice-V projects: exploring RISC-V implementations in Silice](https://github.com/sylefeb/Silice/blob/master/projects/ice-v/README.md)
* [FEMTORV32 / FEMTOSOC: a minimalistic RISC-V CPU](https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV)
* [SERV - The SErial RISC-V CPU](https://github.com/olofk/serv)
* [🖥️ A tiny, customizable and highly extensible MCU-class 32-bit RISC-V soft-core CPU and microcontroller-like SoC written in platform-independent VHDL.](https://github.com/stnolting/neorv32)
* [✔️Port of RISCOF to verify the NEORV32 Processor's RISC-V ISA compatibility.](https://github.com/stnolting/neorv32-riscof)
* [📁 NEORV32 projects and exemplary setups for various FPGAs, boards and (open-source) toolchains.](https://github.com/stnolting/neorv32-setups)
* [User Guide The NEORV32 RISC-V Processor](https://stnolting.github.io/neorv32/ug/)
* [GitHub - litex-hub/linux-on-litex-vexriscv: Linux on LiteX-VexRiscv](https://github.com/litex-hub/linux-on-litex-vexriscv)

---

* [RISC-V SoftCPU Contest Highlights – RISC-V International](https://riscv.org/blog/2018/12/risc-v-softcpu-contest-highlights/)
* [SpinalHDL/VexRiscvSoftcoreContest2018](https://github.com/SpinalHDL/VexRiscvSoftcoreContest2018)
* [SoftCPU/SoC engine-V](https://github.com/micro-FPGA/engine-V)
* [PulseRain Reindeer - RISCV RV32IM Soft CPU](https://github.com/PulseRain/Reindeer)
* [SERV - The SErial RISC-V CPU](https://github.com/olofk/serv)
* [RudolV: RISC-V processor](https://github.com/bobbl/rudolv)
* [JiVe: Small micro-coded RISC-V softcore](https://github.com/fredrequin/JiVe)
* [Featherweight RISC-V implementation](https://github.com/Featherweight-IP/fwrisc)

---

* [riscv-non-isa/riscv-arch-test](https://github.com/riscv-non-isa/riscv-arch-test)
* [Risc-V Assembly](https://youtu.be/GWiAQs4-UQ0?si=RvFJqRN5h1U0tYY6)
* [mini-rv32ima: A tiny C header-only risc-v emulator.](https://github.com/cnlohr/mini-rv32ima)
* [pico-rv32ima: Running Linux on RP2040 with the help of RISC-V emulation](https://github.com/tvlad1234/pico-rv32ima)
* [rv RV32IMC in ~600 lines of C89](https://github.com/mnurzia/rv)
* [TinyEMU is a system emulator for the RISC-V](https://bellard.org/tinyemu/)
* [rvemu: RISC-V emulator for CLI and Web written in Rust with WebAssembly. It supports xv6 and Linux (ongoing).](https://github.com/d0iasm/rvemu)
* [Writing a RISC-V Emulator in Rust - Writing a RISC-V Emulator in Rust](https://book.rvemu.app)
* [rvemu-for-book: Reference implementation for the book "Writing a RISC-V Emulator in Rust".](https://github.com/d0iasm/rvemu-for-book)
* [Writing a simple RISC-V emulator in plain C (Base integer, multiplication and csr instructions) — fmash16's blog](https://fmash16.github.io/content/posts/riscv-emulator-in-c.html)
 
---

* [The Zephyr Project – A proven RTOS ecosystem, by developers, for developers.](https://www.zephyrproject.org)
* [RISC-V International – RISC-V: The Open Standard RISC Instruction Set Architecture](https://riscv.org)
* [RISC-V Boards — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/boards/riscv/index.html)
* [NEORV32 — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/boards/riscv/neorv32/doc/index.html)
* [LiteX VexRiscv — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/boards/riscv/litex_vexriscv/doc/index.html)
* [RISCV32 Emulation (QEMU) — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/boards/riscv/qemu_riscv32/doc/index.html)
* [Introduction — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/introduction/index.html)
* [Raspberry Pi Pico — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/boards/arm/rpi_pico/doc/index.html#)

### Other

create top.v

```verilog
module top (
    input BIN1,
    input BIN2,
    output LED1,
);

    assign LED1 = BIN1 & BIN2;

endmodule
```

No breaks between the commands, treat as one block

```yosys
read_verilog top.v # to convert Verilog
opt # optimise the optput
show # generate a visual representation in a dot file
synth_ice40 # synthesize the design
show # another diagram of the result
cd top # 'cd' into the top module
dump $67 # to view a representation of the design
exit # leave yosys, say before working on another verilog file
write_json top.json # generate json file for the place and route tool, nextpnr
```

## nextpnr

Follow the [vcpkg](https://github.com/microsoft/vcpkg) installation instructions

then:

`vcpkg install boost-filesystem:x64-windows boost-program-options:x64-windows boost-thread:x64-windows boost-python:x64-windows qt5-base:x64-windows eigen3:x64-windows`

Download the [Embeddable python zip file](https://www.python.org/ftp/python/3.6.4/python-3.6.4-embed-win32.zip) for the version compatible with vcpkg from [Python 3.6.4](https://www.python.org/downloads/release/python-364/)

C:/Users/jackc/git/vcpkg and not c:/vcpkg

cmake -DARCH=ice40 -DICEBOX_ROOT=C:/ProgramData/icestorm/share/icebox -DCMAKE_TOOLCHAIN_FILE=C:/Users/jackc/git/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -G "Visual Studio 15 2017 Win64" -DPYTHON_EXECUTABLE=C:/Python364/python.exe -DPYTHON_LIBRARY=C:/Users/jackc/git/vcpkg/packages/python3_x64-windows/lib/python36.lib -DPYTHON_INCLUDE_DIR=C:/Users/jackc/git/vcpkg/packages/python3_x64-windows/include/python3.6 cmake --build . --config Release

## nMigen

I created a specific Python environment in [Anaconda](https://www.anaconda.com/) for my [nMigen](https://github.com/m-labs/nmigen) [installation](https://github.com/m-labs/nmigen#installation).

[How to Manually Install Python Packages - ActiveState](https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/#:~:text=Download%20the%20package%20and%20extract,is%20to%20implement%20setup.py%20.)

[How to Install and Import Modules in Python 3 | Linode Docs](https://www.linode.com/docs/guides/installing-and-importing-modules-in-python-3/)

```cmd
pip install git+https://github.com/m-labs/nmigen.git
pip install git+https://github.com/m-labs/nmigen-boards.git
# https://github.com/amaranth-lang/amaranth-boards.git
```

## Graphviz VS Code Extension

Graphviz Preview - simple preview
Graphviz Interactive Preview - run "Graphviz Interactive:... " in the *Command Palette*

## Alpine WSL

[Alpine WSL GitHub](https://github.com/agowa338/WSL-DistroLauncher-Alpine)

To allow installation of packages
`Alpine.exe config --default-user root`

for icestorm

build-base clang bison flex readline-dev gawk tcl-dev libffi-dev git mercurial graphviz pkgconfig python python3 python-dev python3-dev libftdi1-dev python3-dev qt5-qtbase qt5-qtbase-dev boost-dev boost-libs boost  cmake

apk add sudo curl
May need `py-pip` for pip
pip3 install xdot

### perhaps

automake eigen

### not available

libreadline-dev | readline-dev
pkg-config | pkgconfig
libftdi-dev | libftdi1-dev
qt5-default | qt5-qtbase

## nextpnr stuff

ubuntu: sudo apt get install libeigen3-dev
cmake -DICEBOX_ROOT=/usr/local/share/icebox  -DARCH=ice40 .

apk add eigen

python-dev  
 doxygen swig

eigen

 python-libs
boost-python3
boost-python2
python-boost
python3-boost
boost-python
boost-python3
boost-python2
boost-python
eigen-dev
eigen3-dev
eigen-libs
eigen3
eigen
eigen-dev

## Graphviz

In another termainal...

Need [Grapviz](https://graphviz.gitlab.io/_pages/Download/Download_windows.html) to display output

Move the extracted files to P:\Tools\graphviz-2.38\release\bin adjust PATH

Run `dot show.dot -Tjpg -O` to convert to jpg with the name `show.dot.jpg`

<!-- markdownlint-disable MD034 -->

<!-- markdownlint-enable MD034 -->