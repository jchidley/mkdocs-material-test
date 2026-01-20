---
date: "2022-03-25"
title: "Radio and Electronics"
tags:
  - electronics
  - radio
  - simulation
  - qspice
---
<!-- markdownlint-disable MD025 -->
# Radio stuf
<!-- markdownlint-enable MD025 -->

## Free Information

* [World Radio History](https://www.worldradiohistory.com/index.htm) espeically the [Techinical Section](https://www.worldradiohistory.com/Home-Tech.htm) and [Elektor Magazine](https://archive.org/details/ElektorMagazine) and [Fun Way into Electronics](https://archive.org/details/funway_into_electronics)
* [Free Electronics Books and Magazines Web Sites](https://youtu.be/eBKRat72TDU?si=PoEnyuolLwT7SHuH)

## Simulation Software

Limits of SPICE (and other simulation). Parastics need to be moddeled. Models of various components are only approximations owing to the manufacturers intellectual property concerns and, probably, desire to reduce simulation complexity.

* [Spectrum Software](https://web.archive.org/web/20230219052113/http://www.spectrum-soft.com/index.shtm)
* [Micro Cap 12 Spice Simulation Sofwtare](http://www.spectrum-soft.com/download/download.shtm) and [here](https://gotroot.ca/spectrum/www.spectrum-soft.com/download/download.html)
* [Micro Cap 12](https://youtu.be/WExvpASP-1c?si=JLN4hbqDsmB-AQVV)
* One among many projects: [DIY Operational Amplifier: Tutorial Project](https://www.electroschematics.com/diy-operational-amplifier/) with [a set of videos](https://youtu.be/Z8JDsvfZjL8?si=OXS8azt1TlsKbOgk)
* [Achieving accurate results with a circuit simulator](https://efabless-production-wordpress.s3.amazonaws.com/wp-content/uploads/Achieving-Accurate-Results-with-a-Circuit-Simulator.pdf)
* [Parasitics on Breadboards](https://www.youtube.com/watch?v=ME2wgVFYgIs&t=366s)
* Every component has parasitics of something else (passive) inductance, capacitance and resistance and these [parasitics start in the MHz region](https://electronics.stackexchange.com/a/382087) which include the very fast edges of things.
* [Parasitics in wires](https://ece.uwaterloo.ca/~mhanis/ece730/lecture2.pdf#:~:text=Wiring%20of%20today%E2%80%99s%20integrated%20circuits%20forms%20a%20complex,propagation%20delay%2C%20or%20equivalently%2C%20a%20drop%20in%20performance.)
* 2pf between sucessive tracks on a breadboard, 1pf if the tracks are separated by one track. 20pf for the power rail tracks. [Breadboard Capacitance](https://www.eevblog.com/forum/blog/eevblog-568-solderless-breadboard-capacitance/)
* [Simulation vs Reality](https://www.youtube.com/watch?v=onlrcEFEDWI) models can be missing from EDA software.  Need to test in real life too. Get a board built.
* [Analog by Design Show](https://www.youtube.com/playlist?list=PL59089C08F42536A4)

* Kyrocera AVX has various [design tools](https://www.kyocera-avx.com/design-tools/) which can be used and inspected online. There are also SPICE models for download.

### General

* [Unbricking a $2,000 Bike With a $10 Raspberry Pi](https://ptx2.net/posts/unbricking-a-bike-with-a-raspberry-pi/) Bluetooth Zwift Ant+ Raspberry Pi speed cadence heart rate sensor
* [DIY Operational Amplifier schematic, explanation](https://www.electroschematics.com/diy-operational-amplifier/)

### YouTube

[Electronics with Professor Fiore](https://www.youtube.com/@ElectronicswithProfessorFiore) with [free books](https://www2.mvcc.edu//users/faculty/jfiore/index.cfm)

## QSPICE

finding models

Micro-Cap 12 from Spectrum software has a lot of models included.

It's `mc12cd.zip_Spectrum_Software_Spice_Simulator_12.2.0.5.zip` on my OneDrive.

```bash
# assumes model begins with '.model' and continues with '\n+'
# search for "2n222" in "filename"
awk 'BEGIN{IGNORECASE=1} /\.model\s+*2n222/{f=1; print; next} /^\s*[^+]/{f=0} f' filename 
# I think f is being used to do the default action (print) or nothing
# for a one liner add 
find -type f -print0 | xargs -0 # before awk and drop the "filename", use -r for recursive
```

* [Mike Engelhardt the Creator of LTspice and now QSPICE](https://www.youtube.com/watch?v=5gMVOmkXDVs)
ctrl-enter to add lines to an exisiting text(spice directive). `qsch` are 8-bit encoded [Windows-1252 or CP-1252](https://en.wikipedia.org/wiki/Windows-1252), these can be read in `nvim` or `notepad`. The command reference is in the help informaiton under simulator.
"The analog circuit simulation was originally based on a download of Berkeley SPICE from ptolemy.berkeley.edu. Specifically the version of 3F5 available in early 2020", [documentaiton appears to be at](http://bwrcs.eecs.berkeley.edu/Classes/IcBook/SPICE/) and there's [All about Circuits documentation too](https://www.allaboutcircuits.com/textbook/reference/chpt-7/fundamentals-spice-programming/). Apparently it's normal for it to be cryptic and undocumented. I know that some syntax has been lifted from elsewhere.

* Helpful [guides](https://github.com/KSKelvin-Github/Qspice/tree/main/Guideline)

To get operating point data "File->Export Data" from the *Waveform Viewer*.

* [PyQspice](https://github.com/Qorvo/PyQSPICE/tree/main)

* [QSPICE: A New Simulator for Electronic Circuits (Part 1)](https://www.powerelectronicsnews.com/qspice-a-new-simulator-for-electronic-circuits-part-1/)

See [Tools, components, symbols, code, etc., for Qorvo's free QSpice circuit simulator](https://github.com/robdunn4/QSpice), [QSpice Forum KSKelvin's Github repo](https://github.com/KSKelvin-Github/Qspice/) and [QSpice Forum Mgyger's GitLab repo](https://gitlab.com/mgyger/qspice-symbols/)

The first few chars in the file, according to Mike Engelhardt, "I put those charactors there so certain e-mail servers don’t convert the contents of the file. QSPICE symbols and schematics look like ASCII, and can be edited in notepad or any other eight-bit clean otherwise “ASCII” editor. But they are not ASCII. So I give the files the same majic number as JPEG. E-mail servers don’t touch the contents of JPEG."

[Extra symbols for qspice](https://gitlab.com/mgyger/qspice-symbols) by Markus Gyger see [additional symbols post in forum](https://forum.qorvo.com/t/additional-symbols/14469)

Apparently [netlists can be used in Kicad](https://electronics.stackexchange.com/questions/676175/can-i-import-a-netlist-into-kicad#:~:text=There%27s%20no%20need%20to%20%22import%22%20anything%20into%20KiCad%3A,you%20generate%20perfect%20schematics%20and%20layouts%20that%20way%21). [Kicad uses S-expressions](https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#:~:text=KiCad%20uses%20an%20s-expression%20file%20format%20for%20symbol,circuit%20boards%2C%20and%20title%20block%20and%20border%20worksheets.)

* [Qspice tutorials, examples and guide](https://github.com/KSKelvin-Github/Qspice/tree/main)
* [Tools, components, symbols, code, etc., for Qorvo's free QSpice circuit simulator.](https://github.com/robdunn3/QSpice/tree/main)
* [QSpice Unleashed: Elevating the LTSpice Legacy in Electronic Simulation](https://www.electromaker.io/blog/article/qtspice-unleashed-elevating-the-ltspice-legacy-in-electronic-simulation)
* Ctrl-Right-Button on waveform to get pp, max, min for a particular waveform - like double click gives crosshairs
* Boost converter example and using a C++ with behavioural Voltage to work out efficiency and power loss. [QSpice Insight with Boost Converter](https://youtu.be/1pUUDxWJIKA?si=lIHKPm4MFvlZWr1F)
* [Description of using C++ with it](https://www.youtube.com/watch?v=Rtt5PPsQGag&t=23s)
* [LTSpice information - useful background to qspice](https://youtu.be/NZNerLq8tHc?si=GzlIQBV7u1B5ebAR)
* [LTSpice by the creator](https://www.youtube.com/watch?v=5gKThjZIj-s)
* [Adding models to QSpice](https://forum.qorvo.com/t/adding-model-files-to-qspice/14962)
* [PyQspice - bindings for Python](https://github.com/Qorvo/PyQSPICE/tree/main)
* [funway into electronics](https://archive.org/details/funway_into_electronics/funway_into_electronics_vol_0_22nd_printing/)
* [World Radio History Techical](https://www.worldradiohistory.com/Home-Tech.htm)

[qspice tutorial](https://www.powerelectronicsnews.com/qspice-a-new-simulator-for-electronic-circuits-part-1/)

Troubleshooting Analog Circuits by Bob Pease

Wires

1) Inductive effects can be ignored if the resistance of the wire is substantial enough – this is the case for long aluminum wires with a small cross section, for example, or if the rise and fall times of the applied signals are slow.
2) When wires are short, the cross section of the wire is large (the interconnect has a low resistivity), a capacitance-only model can be used.  
3) When the separation between neighboring wires is large, or when the wires run together for a short distance, interwire capacitance can be ignored, and all parasitic capacitance can be modeled as capacitance to ground.

## PCB

* [Phil's Lab](https://www.phils-lab.net/) and [his YouTube](https://www.youtube.com/@PhilsLab)
* [PCB Design](https://www.scs.stanford.edu/~zyedidia/docs/pcb/pcb_tutorial.pdf)
* [Rick Hartley’s Reading Recommendation](https://ninedotconnects.com/public_resources/Ricks-Reading-Recommendation.pdf)
* [Watch videos about Electronics, PCB Layout, High Speed, Board Design and more ...](https://www.youtube.com/c/RobertFeranec)
* [How to Achieve Proper Grounding - Rick Hartley](https://www.youtube.com/watch?v=ySuUZEjARPY)

## Links

* [Cross Country Wireless Loop Antenna Amplifier VLF test with 1m diameter coax loop](https://www.youtube.com/watch?v=BAmIyd118Os)
* [WSJT-X User Guide](https://physics.princeton.edu/pulsar/k1jt/wsjtx-doc/wsjtx-main-2.5.4.html#INTRO)
* [Digimode Automatic Propagation Reporter](https://pskreporter.info/)
* [pskmap](https://pskreporter.info/pskmap.html)
* [Weak Signal Propagation Reporter Network](https://www.wsprnet.org/drupal/wsprnet/activity)
* [Most recent QDX posts](https://groups.io/g/QRPLabs/search?ev=0&p=%2C%2Cqdx%2C20%2C2%2C0%2C0&ct=1)
* [QRP Labs](http://qrp-labs.com/)

<!-- markdownlint-disable MD034 -->
https://www.bbc.co.uk/radio/info/frequencies.shtml
https://gqrx.dk/supported-hardware
https://github.com/pa3gsb/Radioberry-2.x
https://sdrplay.com/docs/VirtualHere.pdf
https://www.sdrplay.com/sdrplayhamguides/
https://time.is/
https://www.rtl-sdr.com/demonstrating-radio-frequency-interference-with-an-airspy/
https://www.rtl-sdr.com/extio_rtlsdr-modified-extio-for-sdruno-hdsdr-with-direct-sampling-mode/
https://www.sdrplay.com/community/viewtopic.php?f=5&t=3582&p=11423&hilit=s+meter#p11423
https://www.rtl-sdr.com/forum/viewtopic.php?f=1&t=4710&sid=089336097b3e190ff67e421ba29c1403&start=20
https://electronics.howstuffworks.com/radio-spectrum1.htm
http://www.frequencyfinder.org.uk/
http://www.frequencyfinder.org.uk/AM_Stations.pdf
http://shop.qrp-labs.com/kits/qdx
https://groups.io/g/QRPLabs
<!-- markdownlint-enable MD034 -->