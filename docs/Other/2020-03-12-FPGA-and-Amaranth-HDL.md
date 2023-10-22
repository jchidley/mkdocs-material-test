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

## Projects

* [BUILDING AN 8-BIT CPU ON AN FPGA](https://austinmorlan.com/posts/8bit_breadboard_fpga/)
* [BUILDING AN FPGA COMPUTER: SAP-1](https://austinmorlan.com/posts/fpga_computer_sap1/)
* [BUILDING AN FPGA COMPUTER: SAP-2](https://austinmorlan.com/posts/fpga_computer_sap2/)
* [BUILDING AN FPGA COMPUTER: SAP-3](https://austinmorlan.com/posts/fpga_computer_sap3/)
* [BUILDING AN FPGA COMPUTER: VGA](https://austinmorlan.com/posts/fpga_computer_vga/)
* [BUILDING AN 8-BIT CPU ON A GAME BOY](https://austinmorlan.com/posts/8bit_breadboard_gameboy/)
* [BUILDING AN 8-BIT CPU ON A BREADBOARD](https://austinmorlan.com/posts/8bit_breadboard/)

## stuff


* Catherine @whitequark - developer of Amaranth HDL](https://cohost.org/whitequark)
* [#nmigen on 2020-07-31 — irc logs at freenode.irclog.whitequark.org](https://freenode.irclog.whitequark.org/nmigen/2020-07-31)

### Amaranth HDL Installation, Setup

* [pip install amaranth-yosys](https://pypi.org/project/amaranth-yosys/) The Amaranth HDL Yosys wheels provide a specialized WebAssembly based build of Yosys that runs via wasmtime-py if there is no system-wide Yosys installation, or if that installation is too old.

### HDLs

* [HDLs](https://en.wikipedia.org/wiki/Hardware_description_language)
* [Amaranth](https://amaranth-lang.org/docs/amaranth/latest/) - Python - a few hours ago
* [Silice is an open source language that simplifies prototyping and writing algorithms on FPGA architectures.](https://github.com/sylefeb/Silice.git)
* [SpinalHDL · GitHub](https://github.com/SpinalHDL) - Scala - updated 2 days ago
* Check for Spinal HDL [here](https://tomverbeure.github.io/)
* [Demo - Litex Development Enviroment - Public Docs - Trenz Electronic Wiki](https://wiki.trenz-electronic.de/display/PD/Demo+-+Litex+Development+Enviroment)
* [Chisel/FIRRTL: Home](https://www.chisel-lang.org) - Scala - updated yesterday
* [Chisel pdf book](http://www.imm.dtu.dk/~masca/chisel-book.html)
* [Migen](https://m-labs.hk/migen/manual/index.html#https://m-labs.hk/migen/manual/index.html#) - still getting updates
* [nMigen](https://github.com/m-labs/nmigen-boards.git) - last update 2022
* [MyHDL](https://myhdl.org/) - 31-May-2019 MyHDL 0.11.0 released
* [FOSS Flows For FPGA — F4PGA documentation](https://f4pga.readthedocs.io/en/latest/index.html)

### Amaranth, Migen, nMigen

* [ChipFlow alpha documentation](https://docs.chipflow.io/en/latest/index.html)
* [amaranth: A modern hardware definition language and toolchain based on Python](https://github.com/amaranth-lang/amaranth.git) see [the documentation for Amaranth's Language & toolchain](https://amaranth-lang.org/docs/amaranth/latest/index.html)
* [Implementing a UART in Verilog and Migen — whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-18/implementing-an-uart-in-verilog-and-migen/) and [Implementing a simple SoC in Migen -- whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-19/implementing-a-simple-soc-in-migen/)
* [A (Very) Quick Tour of nMigen as of May 25th, 2021](https://github.com/JosephBushagour/tour-of-nmigen.git)
* [FPGA Pong!](https://github.com/railnova/workshop-FPGA-Pong.git) with some useful explanations
* [amaranth-template-fpga](https://github.com/amaranth-lang/template-fpga)
* [Building FPGA Gateware with Verilog and Amaranth: A Tutorial — CFU-Playground documentation](https://cfu-playground.readthedocs.io/en/latest/crash-course/gateware.html#part-2-amaranth-basics)
* [Migen Litex tutorial](https://github.com/fjullien/migen_litex_tutorials.git) with several PDFs
* [Notes on nMigen](https://41j.com/blog/?s=nmigen)
* [iCEBreaker amaranth examples](https://github.com/icebreaker-fpga/icebreaker-amaranth-examples.git)
* [Learning FPGA Design with nMigen](https://vivonomicon.com/2020/04/14/learning-fpga-design-with-nmigen/) and [github](https://github.com/WRansohoff/nmigen_getting_started.git) and [ice40 flash reader](https://github.com/WRansohoff/nmigen_ice40_spi_flash)
* [Let’s Write a Minimal RISC-V CPU in nMigen – Vivonomicon's Blog](https://vivonomicon.com/2020/06/13/lets-write-a-minimal-risc-v-cpu-in-nmigen/) and [github](https://github.com/WRansohoff/rv32i_nmigen_blog.git)
* [How I went from blinker to RSIC-V in 3 months](https://blog.yosyshq.com/p/blinker-to-risc-v/)
* [bl0x/learn-fpga-amaranth: Code for Bruno Levy's learn-fpga tutorial written in Amaranth HDL](https://github.com/bl0x/learn-fpga-amaranth.git)
* [amaranth | Open Research Institute](https://www.openresearch.institute/tag/amaranth/) with [source code for maia sdr](https://github.com/maia-sdr/maia-sdr.git)
* [Python to HDL: full Amaranth walkthrough to FPGA and ASIC GDS](https://youtu.be/yJxAX7gCpvQ?si=lVHfpUBPbFDDCRz3) with [neptune: Flexible digital logic hardware frequency discriminator used as an extreeeeeme guitar tuner.](https://github.com/psychogenic/neptune.git) and asic [Tiny Tapeout :: Documentation in English](https://tinytapeout.com)
* [learning nmigen](https://libre-soc.org/docs/learning_nmigen/)
* [Stuff about luna and nmigen / amaranth](https://talks.toorcon.net/media/toorcon-2021/question_uploads/Unauthorized_Guide_to_LUNA_xK3u1SN.pptx)
* [nmigen-examples: I want to learn nMigen](https://github.com/kbob/nmigen-examples.git)
* [Graded exercises for Amaranth HDL](https://github.com/RobertBaruch/amaranth-exercises.git) and [Tutorial](https://github.com/RobertBaruch/amaranth-tutorial.git)
* [learning nmigen](https://libre-soc.org/docs/learning_nmigen/)
* [Libre-soc-dev nmigen tutorials etc.](http://lists.libre-soc.org/pipermail/libre-soc-dev/2021-October/003858.html)
* [ULX3S nMigen examples](https://github.com/GuzTech/ulx3s-nmigen-examples.git)
* [Amaranth HDL examples for the Ulx4m FPGA board](https://github.com/lawrie/ulx4m_amaranth_examples.git) 
* [blackicemx_nmigen_examples](https://github.com/lawrie/blackicemx_nmigen_examples.git)
* [hdl_ldpc_encoder](https://github.com/PaulBryden/hdl_ldpc_encoder.git)
* [A simple RISC V CPU built with nMigen](https://github.com/lochsh/riscy-boi.git)
* [Assorted library of utility cores for amaranth HDL](https://github.com/amaranth-farm/amlib.git)
* [mtkCPU is a simple, clear, hackable and very inefficient implementation of RiscV ISA in Amaranth HDL](https://github.com/bieganski/mtkcpu.git)
* [dsp_nmigen](https://github.com/chipmuenk/dsp_nmigen.git)
* [Experimental DSP cores in Amaranth HDL](https://github.com/mndza/dsp_sandbox.git)
* [naps - The Relaxed Amaranth Packages Collection](https://github.com/apertus-open-source-cinema/naps.git) and [FPGA Image Processing](https://apertus-open-source-cinema.github.io/naps/intro.html) and [this poster](https://github.com/apertus-open-source-cinema/naps/blob/main/doc/NapsPosterFPGAIgnite2023.pdf) from [apertus°](https://www.apertus.org/)
* [amaranth examples](https://github.com/adamgreig/amaranth-examples.git)
* [amgen command line tool for frequent amgen HDL tasks (generate sources, show design)](https://github.com/amaranth-farm/amgen.git)
* [in progress 6502 core](https://github.com/mmagm/m6502.git)
* [doing audio/DSP things with nMigen](https://github.com/H-S-S-11/numerically-controlled-oscillator.git)
* [nMigen WISHBONE Examples](https://github.com/cyber-murmel/nmigen-wishbone-examples.git)
* [Icebreaker nMigen Life](https://github.com/alanvgreen/icebreaker-nmigen-life.git)
* [Projects to learn nMigen and Amaranth](https://github.com/gioarchv/learn-amaranth.git)
* [Bellatrix is a CPU core that implements the RISC-V RV32I Instruction Set, based on Minerva](https://github.com/AngelTerrones/Bellatrix.git)
* [Altair is a CPU core that implements the RISC-V RV32I Instruction Set.](https://github.com/AngelTerrones/Altair.git)
* [nmigen-beginner](https://github.com/DonaldKellett/nmigen-beginner.git) from [ZipCPU's site](http://zipcpu.com/tutorial/)
* [Misato RISC-V RV32I CPU](https://github.com/GuzTech/misato.git)
* [amaranth-farm ... where users of amaranth HDL share cores and code with each other](https://github.com/amaranth-farm)
* [Use amaranth-to-litex to simply import Amaranth code into a Litex project](https://github.com/lambdaconcept/amaranth-to-litex.git)
* [An Amaranth implementation of Voja Antonic's 4bit CPU](https://github.com/ylm/nibblecpu.git) and [BADGE FOR SUPERCON.6 / November 2022](https://hackaday.io/project/182568/files)
* [RISC-V processor implemented in Amaranth](https://github.com/msvisser/riscv-tilelink.git)
* [A simple fixed-point FFT module with amaranth](https://github.com/kazkojima/tinyfft-fpga.git)
* [Streams library for Amaranth](https://github.com/DaveBerkeley/streams.git)
* [Implementation of CORDIC (COordinate Rotation DIgital Computer)in Amaranth ](https://github.com/DaveBerkeley/cordic.git)
* [based on icebreaker-amaranth-examples](https://github.com/cyber-murmel/amaranth-examples.git)
* [It's a UART... written in Amaranth!](https://github.com/cr1901/amaranth_uart.git)
* [MCH2022 badge amaranth examples](https://github.com/cyber-murmel/mch2022-amaranth-examples.git)
* [A collection of experimentations using the amaranth HDL framework](https://github.com/sporniket/amaranth_sandbox.git)
* [A curated collection of code written using the amaranth hdl](https://github.com/sporniket/amaranth-stuff.git)
* [simple risc-v cpu and soc in amaranth-lang](https://github.com/vdbhatt/nutty.git)
* [An implementation of "the cradle" for the ECP5-based colorlight i9 written with the Amaranth HDL](https://github.com/sporniket/the-cradle-colorlight-i9-ecp5-amaranth-hdl)
* [Small, FPGA soft-cores for multiplication, division (eventually), and other arithmetic](https://github.com/cr1901/smolarith.git)
* [An FPGA project that implements the memory map of the computer known as Atari STe](https://github.com/sporniket/the-cradle-colorlight-i9-ecp5-amaranth-hdl.git)
* [Standard HyperRAM core for ECP5](https://github.com/gregdavill/litex-hyperram.git)
* [Fiddling with FPGAs, Migen, LiteX and stuffs](https://github.com/titouanc/fpga-scratchpad.git) including ULX3S
* [learn-migen: migen tutorials, etc](https://github.com/jonnew/learn-migen.git)
* [(WIP) FSM generator for Migen based on Python generators](https://github.com/cactorium/fsm-gen-migen.git)
* [nMigen for 6800 CPU](https://www.youtube.com/watch?v=AQOXoKQhG3I&list=PL2Bqmy_B2P9t8sFYz39OC9eWEAke7E3nt&index=30) with [source code](https://github.com/RobertBaruch/n6800.git)
* [Monitor signals MyHDL/nMigen simulation and display as waveforms in a Jupyter notebook](https://github.com/devbisme/myhdlpeek.git) 
* [serialcommander is a small nmigen tool that executes various 'tasks' when sent various characters over a serial port/UART](https://github.com/newhouseb/serialcommander.git)
* [Amaranth-HDL built movement engine](https://github.com/hstarmans/hexastorm/blob/master/src/hexastorm/movement.py) [hexastorm](https://github.com/hstarmans/hexastorm.git) uses amaranth elsewhere and the movement is [based on this paper](http://www.roboticsproceedings.org/rss10/p42.pdf) 
* [More Amaranth HDL stuff with `*.v` files, Klipper too](https://github.com/sensille/conan_fpga.git)

---

* [Introduction -- LUNA documentation](https://luna.readthedocs.io/en/latest/intro.html)
* [GitHub - greatscottgadgets/luna: a USB multitool + Amaranth HDL framework for monitoring, hacking, and developing USB devices](https://github.com/greatscottgadgets/luna.git)
* [Cynthion - Great Scott Gadgets](https://greatscottgadgets.com/cynthion/)

search for Amaranth / nMigen / Migen with language Python at GitHub

### Tutorials, Examples

* [FPGA Introduction](https://youtube.com/playlist?list=PL3by7evD3F52On-ws9pcdQuEL-rYbNNFB&si=dVFTdoYEmnfezTvN)
* [FPGA-101: Introduction to FPGAs, Learn the Basics](https://nandland.com/fpga-101/)
* [Getting Started with FPGAs | No Starch Press](https://nostarch.com/gettingstartedwithfpgas)
* [Introductory Digital Systems Laboratory](https://web.mit.edu/6.111/www/f2016/)
* [HDL workflow](https://libre-soc.org/HDL_workflow/)
* [fpgacpu.org - FPGA CPU News](http://www.fpgacpu.org/index.html)
* [assembly - Implementation of simple microprocessor using verilog - Stack Overflow](https://stackoverflow.com/questions/51592244/implementation-of-simple-microprocessor-using-verilog/51621153#51621153)
* [GitHub - BrunoLevy/learn-fpga: Learning FPGA, yosys, nextpnr, and RISC-V](https://github.com/BrunoLevy/learn-fpga.git/tree/master)
* [Yosys Headquarters · GitHub](https://github.com/YosysHQ)
* [YosysHQ Documentation Library](https://yosyshq.readthedocs.io/en/latest/index.html#yosyshq-documentation-library)
* [oss-cad-suite-build: Multi-platform nightly builds of open source digital design and verification tools](https://github.com/YosysHQ/oss-cad-suite-build)

* [Circuit Simulator Applet](http://falstad.com/circuit/)
* [FPGA Bootcamp #0 | Hackaday.io](https://hackaday.io/project/159720-fpga-bootcamp-0)
* [Implementing a UART in Verilog and Migen — whitequark's lab notebook](https://lab.whitequark.org/notes/2016-10-18/implementing-an-uart-in-verilog-and-migen/)
* [Designing a RISC-V CPU, Part 1: Learning hardware design as a software engineer](https://mcla.ug/blog/risc-v-cpu-part-1.html)
* [migen:tutorial](https://web.archive.org/web/20180813074637/http://blog.lambdaconcept.com/doku.php?id=migen:tutorial)
* [Including non-Amaranth Instances in Amaranth - kate's lab notebook](https://lab.ktemkin.com/post/amaranth-instance/)
* [fpga4fun.com - where FPGAs are fun](https://www.fpga4fun.com)
* [litex FPGA 101 lessons/labs](https://github.com/litex-hub/fpga_101.git)
* [Reuse a (System)Verilog, VHDL, (n)Migen, Spinal HDL, Chisel core](https://github.com/enjoy-digital/litex/wiki/)Verilog,-VHDL,-(n)Migen,-Spinal-HDL,-Chisel-core)
* [GitHub - osresearch/up5k: Upduino v2 with the ice40 up5k FPGA demos](https://github.com/osresearch/up5k.git)
* [🎲 A Tiny and Platform-Independent True Random Number Generator for any FPGA.](https://github.com/stnolting/neoTRNG.git)
* [learn-fpga: Learning FPGA, yosys, nextpnr, and RISC-V](https://github.com/BrunoLevy/learn-fpga.git)
* [Building risc on FPGA](http://www.fpgacpu.org/papers/xsoc-series-drafts.pdf)
* [Icestudio Documentation](https://github.com/FPGAwars/icestudio/wiki)

### Verilog

* [GitHub - johnwinans/Verilog-Examples](https://github.com/johnwinans/Verilog-Examples.git)
* [Learning how to FPGA with ‘Neopixel’ LEDs – Vivonomicon's Blog](https://vivonomicon.com/2018/12/24/learning-how-to-fpga-with-neopixel-leds/)

#### old but useful

* [Porting a New Board To Migen](https://www.wdj-consulting.com/blog/migen-port/)
* [Migen Tutorial](https://m-labs.hk/docs/migen-tutorial.pdf)
* [Migen manual — Migen 0.8.dev0 documentation](https://m-labs.hk/migen/manual/)
* [Migen | M-Labs](https://m-labs.hk/gateware/migen/)

probably worth looking up Migen documentation

### Hardware

* [A Student’s Guide to the Digital World](https://web.mit.edu/6.111/www/f2017/handouts/TheDigitalWorld.pdf)
* [nextpnr](https://www.youtube.com/watch?v=LiCQzQsLFqA)
* [Exploring Open-Toolchain FPGA HW, part 1](https://www.ktemkin.com/exploring-open-fpga-hardware/)

[Zero to ASIC Course | Zero to ASIC Course](https://www.zerotoasiccourse.com)
[ChipFlow alpha documentation](https://docs.chipflow.io/en/latest/index.html)

Boards that I own:
* TinyFPGA BX ICE40LP8K 128 KBit RAM, 6000 KBit flash
* TinyFPGA A2 XO2-1200 64 KBit RAM 64 KBit flash
* iceFUN iCE40-HX8K 
* XLX3S Lattice ECP5 LFE5U-85F-6BG381C 32MB SDRAM, 4-16 MB Quad-SPI Flash 
* upduino 2.1 Lattice UltraPlus ICE40UP5K FPGA with 5.3K LUTs, 1Mb SPRAM, 120Kb DPRAM, 8 Multipliers

All supported by [Apio (pronounced [ˈa.pjo]) is a multiplatform toolbox](https://github.com/FPGAwars/apio.git)
ULX3S, TinyFPGA BX supported by [Litex](https://github.com/litex-hub/litex-boards.git)
ULX3S, Upduino

* [UPduino Documentation — UPduino 0.1 documentation](https://upduino.readthedocs.io/en/latest/index.html)
* [TinyFPGA](https://tinyfpga.com/)
* [ULX3S](https://www.crowdsupply.com/radiona/ulx3s) and [ulx3s](https://ulx3s.github.io/)
* [GitHub - devantech/iceFUN](https://github.com/devantech/iceFUN.git) and [Datasheet pdf](https://www.robot-electronics.co.uk/files/iceFUNdoc.pdf) and [programmer](https://github.com/dorssel/usbipd-win)
* [First steps with openFPGALoader](https://trabucayre.github.io/openFPGALoader/guide/first-steps.html)
* [deprecated in favor of openFPGALoader](https://github.com/kost/fujprog.git)

[2057-ICE40HX4K-TQ144-breakout: Minimal Raspberry PI breakout board for ICE40HX4K FPGA](https://github.com/johnwinans/2057-ICE40HX4K-TQ144-breakout.git) and [this video](https://youtu.be/yWLgxug_TMk?si=k8TgFi94GnOfyN03)
ICE40 HX 4k appears to be an 8K with different packaging, [under £8 each](https://www.mouser.co.uk/ProductDetail/Lattice/iCE40HX4K-TQ144?qs=F9A14TELRMvGNTZXkNDuOw%3D%3D)


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

Follow the [vcpkg](https://github.com/microsoft/vcpkg.git) installation instructions

then:

`vcpkg install boost-filesystem:x64-windows boost-program-options:x64-windows boost-thread:x64-windows boost-python:x64-windows qt5-base:x64-windows eigen3:x64-windows`

Download the [Embeddable python zip file](https://www.python.org/ftp/python/3.6.4/python-3.6.4-embed-win32.zip) for the version compatible with vcpkg from [Python 3.6.4](https://www.python.org/downloads/release/python-364/)

C:/Users/jackc/git/vcpkg and not c:/vcpkg

cmake -DARCH=ice40 -DICEBOX_ROOT=C:/ProgramData/icestorm/share/icebox -DCMAKE_TOOLCHAIN_FILE=C:/Users/jackc/git/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -G "Visual Studio 15 2017 Win64" -DPYTHON_EXECUTABLE=C:/Python364/python.exe -DPYTHON_LIBRARY=C:/Users/jackc/git/vcpkg/packages/python3_x64-windows/lib/python36.lib -DPYTHON_INCLUDE_DIR=C:/Users/jackc/git/vcpkg/packages/python3_x64-windows/include/python3.6 cmake --build . --config Release

## nMigen

I created a specific Python environment in [Anaconda](https://www.anaconda.com/) for my [nMigen](https://github.com/m-labs/nmigen-boards.git) [installation](https://github.com/m-labs/nmigen#installation).

[How to Manually Install Python Packages - ActiveState](https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/#:~:text=Download%20the%20package%20and%20extract,is%20to%20implement%20setup.py%20.)

[How to Install and Import Modules in Python 3 | Linode Docs](https://www.linode.com/docs/guides/installing-and-importing-modules-in-python-3/)

```cmd
pip install git+https://github.com/m-labs/nmigen-boards.git.git
pip install git+https://github.com/m-labs/nmigen-boards.git-boards.git
```

```bash
sudo apt -y install python3-pip gtkwave
```

```PS
wsl -t U3
wsl -d U3
```

```bash
# https://github.com/YosysHQ/oss-cad-suite-build
# wget https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2023-09-25/oss-cad-suite-linux-x64-20230925.tgz
cd ~
tar -xvf /mnt/c/Users/jackc/Downloads/oss-cad-suite-linux-x64-20230925.tgz -C ~
# source oss-cad-suite/environment # every time
sudo cp ~/oss-cad-suite/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
sudo usermod -a -G plugdev $USER # might need to logout/login
cat << "EOF" >> ~/.profile

# set PATH so it includes user's oss-cad-suite/bin
if [ -d "$HOME/oss-cad-suite/bin" ] ; then
export PATH="$HOME/oss-cad-suite/bin:$PATH"
fi
EOF
. ~/.profile
```

```bash
pip3 install --upgrade amaranth
pip3 install --upgrade pip # otherwise amaranth-boards installs as UKNOWN
# git clone https://github.com/amaranth-lang/amaranth.git-boards.git
# cd amaranth-boards
# python3 -m pip install .
pip3 install --upgrade git+https://github.com/amaranth-lang/amaranth.git-boards.git
pip install markupsafe==2.0.1 # fixes ImportError: cannot import name 'soft_unicode' from 'markupsafe'...
```

[ImportError: cannot import name 'soft_unicode' from 'markupsafe'](https://stackoverflow.com/questions/72191560/importerror-cannot-import-name-soft-unicode-from-markupsafe)

```PS
# usbipd wsl detach --all
# usbipd list
usbipd wsl attach --busid 1-2 --distribution U3
```

```bash
python3 -m amaranth_boards.ulx3s 85F
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
