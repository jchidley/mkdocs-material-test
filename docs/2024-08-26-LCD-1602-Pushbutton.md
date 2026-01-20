---
date: "2024-08-26"
title: "LCD 1602 Keypad Shield"
tags:
  - arduino
  - embedded
  - hardware
---
<!-- markdownlint-disable MD025 -->
# LCD 1602 Pushbutton
<!-- markdownlint-enable MD025 -->

## Introduction

I bought this [Keypad Shield LCD 1602 Module Display Arduino ATMEGA328 ATMEGA2560 (E101)](https://www.ebay.co.uk/itm/354881979735) which references [LCD1602KeyPad](https://github.com/christiangda/LCD1602KeyPad) Github repository.

It's based on "HD44780 parallel interface chipset" and [this is Hitachi's datasheet](https://www.sparkfun.com/datasheets/LCD/HD44780.pdf)

Arduino has a [tutorial for LCD displays](https://docs.arduino.cc/learn/electronics/lcd-displays/) like this and someone wrote a driver for the eBay item referenced above [D1RobotLCDKeypadShieldArduinoUno](https://github.com/mich1342/D1RobotLCDKeypadShieldArduinoUno/tree/master). It appears to be a knock off of [DF Robot's design](https://wiki.dfrobot.com/LCD_KeyPad_Shield_For_Arduino_SKU__DFR0009)

[Electropeak has a nice tutorial](https://electropeak.com/learn/using-1602-character-lcd-keypad-shield-arduino/)

Someone wrote an [Arduino library for the chipset](https://github.com/duinoWitchery/hd44780) and there's this [recent rust embedded driver](https://github.com/JohnDoneth/hd44780-driver) and an older [rust library](https://docs.rs/lcd/latest/lcd/).

For the Pi Pico the pin numbers are used as is (0, 1, etc) for A0..A3 reserved for analog.


