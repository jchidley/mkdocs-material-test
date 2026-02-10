---
date: "2023-05-01"
title: "VFD 3-Phase Converter"
tags:
  - electronics
  - modbus
  - vfd
---
<!-- markdownlint-disable MD025 -->
# VFD 3 Phase Converter
<!-- markdownlint-enable MD025 -->

## Introduction

Modbus RTU using RS485 using commix 1.4 software from the PC.
https://geekmonkey.org/lwm-julia-bitwise-operators/ includes CRC and a reference to Hacker's delight
also 
pkg add CRC
using CRC
crc32 = crc(CRC_32)
```julia
crcmodbus = CRC.crc(CRC.CRC_16_MODBUS)

#11 03 006B 0003 7687
msg = [0x11,0x03,0x00,0x6B,0x00,0x03]
crcmodbus(msg) # 0x8776 
# idential to https://www.lammertbies.nl/comm/info/crc-calculation
# reported 76 87 https://ipc2u.com/articles/knowledge-base/modbus-rtu-made-simple-with-detailed-descriptions-and-examples/
# little vs big endian
# https://stackoverflow.com/questions/65734589/understand-modbus-rtu-crc#:~:text=In%20document%20of%20Modbus%20protocol,values%20for%20the%20low%20byte.%22

msg = [0x11,0x02,0x03,0xac,0xdb,0x35] 
crcmodbus(msg) # 0x1820 vs 2018 from https://ipc2u.com/articles/knowledge-base/modbus-rtu-made-simple-with-detailed-descriptions-and-examples/
```

Julia `using CRC32c; crc32c("one")`

## Links

* [See appendices for 485 CAN bus etc](https://docs.galco.com/techdoc/dlpc/driv_ac_vfd-e_um.pdf) — Technical user manual for Delta's VFD-E Series variable frequency drive (AC motor drive), covering installation, wiring, parameter settings, troubl...
* [Online CRC Calculator](https://www.lammertbies.nl/comm/info/crc-calculation) — This page provides an online CRC (Cyclic Redundancy Check) calculator and explains the mathematical principles behind CRC calculations for error de...
* [VFD](https://realpars.com/variable-frequency-drive/)
* [VFD Configuration](https://wiki.printnc.info/en/controllers/linuxcnc/vfd) — A technical guide for configuring Huanyang VFD (Variable Frequency Drive) spindle control via RS485/Modbus communication with LinuxCNC, covering wi...
* [VFD info](http://www.softstartuk.com/wp-content/uploads/2013/07/VFD-E-Modbus-RTU-SS.pdf)
* [Modbus](https://en.wikipedia.org/wiki/Modbus) — Modbus is a client/server communication protocol originally designed in 1979 for programmable logic controllers (PLCs) that has become a de facto s...
* [Details on codes to send to VFD  ](https://www.ato.com/how-to-control-vfd-via-rs485-interface) — A tutorial demonstrating how to remotely control a Variable Frequency Drive (VFD) using the RS485 interface with Modbus RTU protocol, including wir...
* [VFD Control Methods](https://www.ato.com/5-frequency-control-methods-for-vfd) — This article describes five methods for controlling Variable Frequency Drive (VFD) frequency to manage AC motor speed: button control, analog contr...
* [RS485 vs Modbus Protocol. RS485 communication tutorial](https://www.eltima.com/article/modbus-vs-rs485/) — This article explains the difference between RS485 and Modbus: RS485 defines the physical signal level for serial communication, while Modbus defin...
* [Modbus vs RS485 | A quick tutorial on RS485 and MODBUS](https://www.virtual-serial-port.org/articles/modbus-vs-rs485/) — A technical tutorial explaining RS485 serial communication protocol and its relationship with Modbus, covering half-duplex transmission, master/sla...
* [Modbus RTU Protocol Overview - Real Time Automation, Inc.](https://www.rtautomation.com/technologies/modbus-rtu/) — Modbus RTU is an open serial communication protocol originally developed by Modicon (now Schneider Electric) that uses RS-232 or RS-485 interfaces ...
* [Modbus RTU made simple with detailed descriptions and examples](https://ipc2u.com/articles/knowledge-base/modbus-rtu-made-simple-with-detailed-descriptions-and-examples/) — A comprehensive tutorial explaining the Modbus RTU industrial communication protocol, covering its message structure, register types, function code...