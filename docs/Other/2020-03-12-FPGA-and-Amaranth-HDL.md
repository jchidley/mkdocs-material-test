---
date: "2020-03-12"
title: "FPGA-and-Amaranth-HDL"
---
<!-- 2020-03-12-Toolchain.md -->

<!-- markdownlint-disable MD025 -->
# FPGA and Amaranth HDL
<!-- markdownlint-enable MD025 -->

## Introduction

For a whole stack of reasons, mostly gleaned from [this playlist](https://youtube.com/playlist?list=PL3by7evD3F52On-ws9pcdQuEL-rYbNNFB&si=8EmvqcqfRbyXapf0) and earlier reading (prior to 2023) it seems like this is the way to go:

* Verilog
* Simulation, not physical hardware
* ICE40 HX 4K
* Icestorm 
* Risc-V
* 6502 

John uses Z80 as it was his first computer, 6502 is, arguably, easier to understand and implement. There will also be a number of soft-cores of the 6502 and a lot of assembly examples - this is what people programmed in.

## stuff

ICE40 HX 4k appears to be an 8K with different packaging, [under £8 each](https://www.mouser.co.uk/ProductDetail/Lattice/iCE40HX4K-TQ144?qs=F9A14TELRMvGNTZXkNDuOw%3D%3D)

[GitHub - johnwinans/Verilog-Examples](https://github.com/johnwinans/Verilog-Examples)

[2057-ICE40HX4K-TQ144-breakout: Minimal Raspberry PI breakout board for ICE40HX4K FPGA](https://github.com/johnwinans/2057-ICE40HX4K-TQ144-breakout/tree/master)

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


### Amaranth HDL Installation, Setup

* [pip install amaranth-yosys](https://pypi.org/project/amaranth-yosys/) The Amaranth HDL Yosys wheels provide a specialized WebAssembly based build of Yosys that runs via wasmtime-py if there is no system-wide Yosys installation, or if that installation is too old.
[ImportError: cannot import name 'soft_unicode' from 'markupsafe'](https://stackoverflow.com/questions/72191560/importerror-cannot-import-name-soft-unicode-from-markupsafe)

### WSL

* [Awesome-WSL: Awesome list dedicated to Windows Subsystem for Linux](https://github.com/sirredbeard/Awesome-WSL#10-gui-apps)
* [How to add second WSL2 Ubuntu distro](https://superuser.com/questions/1515246/how-to-add-second-wsl2-ubuntu-distro-fresh-install)
* [ubuntu images](https://cloud-images.ubuntu.com/wsl/)
* [How to change default user in WSL Ubuntu bash on Windows 10](https://askubuntu.com/questions/816732/how-to-change-default-user-in-wsl-ubuntu-bash-on-windows-10)
* [WSL - Connect USB devices](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
* [usbipd-win](https://github.com/dorssel/usbipd-win)
 
### HDLs

* [Silice is an open source language that simplifies prototyping and writing algorithms on FPGA architectures.](https://github.com/sylefeb/Silice/tree/master)
* [SpinalHDL · GitHub](https://github.com/SpinalHDL)
* [Demo - Litex Development Enviroment - Public Docs - Trenz Electronic Wiki](https://wiki.trenz-electronic.de/display/PD/Demo+-+Litex+Development+Enviroment)
* [Chisel/FIRRTL: Home](https://www.chisel-lang.org)

### Tutorials, Examples

* [FPGA Introduction](https://youtube.com/playlist?list=PL3by7evD3F52On-ws9pcdQuEL-rYbNNFB&si=dVFTdoYEmnfezTvN)
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
* [Implementing a UART in Verilog and Migen — whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-18/implementing-an-uart-in-verilog-and-migen/)
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
* [Icestudio Documentation](https://github.com/FPGAwars/icestudio/wiki)
* [Learning FPGA Design with nMigen](https://vivonomicon.com/2020/04/14/learning-fpga-design-with-nmigen/)

#### old but useful

* [Porting a New Board To Migen](https://www.wdj-consulting.com/blog/migen-port/)
* [Migen Tutorial](https://m-labs.hk/docs/migen-tutorial.pdf)
* [Migen manual — Migen 0.8.dev0 documentation](https://m-labs.hk/migen/manual/)
* [Migen | M-Labs](https://m-labs.hk/gateware/migen/)

probably worth looking up Migen documentation

### Hardware

* [UPduino Documentation — UPduino 0.1 documentation](https://upduino.readthedocs.io/en/latest/index.html)
* [ULX3S | Crowd Supply](https://www.crowdsupply.com/radiona/ulx3s) and [ulx3s](https://ulx3s.github.io/)
* [GitHub - devantech/iceFUN](https://github.com/devantech/iceFUN) and [Datasheet pdf](https://www.robot-electronics.co.uk/files/iceFUNdoc.pdf) and [programmer](https://github.com/dorssel/usbipd-win)
* [First steps with openFPGALoader](https://trabucayre.github.io/openFPGALoader/guide/first-steps.html)
* [deprecated in favor of openFPGALoader](https://github.com/kost/fujprog)

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