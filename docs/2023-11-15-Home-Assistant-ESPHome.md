---
date: "2023-11-15"
title: "Home-Assistant-ESPHome"
---
<!-- markdownlint-disable MD025 -->
# Template
<!-- markdownlint-enable MD025 -->

## Home Assistant

* [Understanding MQTT Topics](http://www.steves-internet-guide.com/understanding-mqtt-topics/)
* [Scargill Tech Blog](https://tech.scargill.net/)
* [A simple setup for your own smart home server (on a Raspberry Pi)](https://github.com/OliverHi/smarthomeserver)
* [Home Assistant Container](https://sequr.be/blog/2021/08/home-assistant-container-part-1-install-debian-docker-and-portainer/)
* [Random Light Schedule on Home Assistant](https://community.home-assistant.io/t/random-light-schedule/10134/16)
* [Home Assistant Configuration Example](https://github.com/arsaboo/homeassistant-config)
* [How much does it cost to run a smart home?](https://notenoughtech.com/home-automation/smart-lights-wont-save-you-money/#google_vignette)

## Links

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->
* [Firmware, etc on Sonoff BasicR4](https://notenoughtech.com/home-automation/sonoff-basicr4/)
* [Tutorial on making a ESPHome External Component from scratch](https://community.home-assistant.io/t/tutorial-on-making-a-esphome-external-component-from-scratch/592758) and [HomeThing](https://homething.io/)
* [Build your own CT Clamp Power and Energy Monitor with ESPHome](https://youtu.be/fvCqXjey8lI?si=8ripOyHlnpB_znNG)
* [Loads of interesting ESP8266 ESP32 products](https://www.mottramlabs.com/esp_products.html)
* [MAKE AN ARDUINO TEMPERATURE SENSOR (THERMISTOR TUTORIAL)](https://www.circuitbasics.com/arduino-thermistor-temperature-sensor-tutorial/)
* [HOW ROTARY ENCODERS WORK – ELECTRONICS BASICS](https://www.thegeekpub.com/245407/how-rotary-encoders-work-electronics-basics/)
* [Incremental encoder](https://en.wikipedia.org/wiki/Incremental_encoder)
* [Rpi pico w onboard temperature sensor and onboard led](https://community.home-assistant.io/t/rpi-pico-w-onboard-temperature-sensor-and-onboard-led/564904/3)
* [pico-w-garage-door-sensor](Raspberry Pi Pico W Garage Door Sensor)
* [Using ESPHome on the Raspberry Pi Pico W and other RP2040 microcontroller boards](https://koen.vervloesem.eu/blog/using-esphome-on-the-raspberry-pi-pico-w-and-other-rp2040-microcontroller-boards/)
* [Development for Home Assistant](https://developers.home-assistant.io/docs/development_index) and [my fork of Home Assistant](https://github.com/jchidley/core)
* This is the normal Home Assistant documentation for [examples of Home Assistant custom config](https://github.com/home-assistant/example-custom-config/tree/master) this will work with [ESPHome](https://esphome.io/custom/custom_component.html) but they prefer that you use [exernal components](https://esphome.io/components/external_components) but the documentation for external components is severely limited, as of 2023
* [Electro Dragon Relay](https://templates.blakadder.com/electrodragon_relay.html)
* [WAGO 24A LIGHT JUNCTION BOX 39 X 95 X 29MM GREY](https://www.screwfix.com/p/wago-24a-light-junction-box-39-x-95-x-29mm-grey/8423f)
* Cheap EARU Electric TV01 No WIFI[Programmable Thermostat Timer TRV Radiator Valve Actuator Temperature Controller](https://www.aliexpress.com/item/1005005481063949.html?aff_platform=true&aff_short_key=UneMJZVf&isdl=y&src=bing&pdp_npi=3%40dis%21GBP%2127.92%2127.92%21%21%210%21%21%40%2112000033272360876%21ppc%21%21&albch=shopping&acnt=135095331&isdl=y&albcp=373871297&albag=1310618086885310&slnk=&trgt=pla-4585513247789238&plac=&crea=81913680283612&netw=o&device=c&mtctp=e&utm_source=Bing&utm_medium=shopping&utm_campaign=PA_Bing_UK_PC_customlabel1&utm_content=customlabel1%3D7&utm_term=programmable%20trv&msclkid=bf8f20514b5c1a443cb74501d93d1a63)
* [Purpose of the diode and capacitor in this motor circuit](https://electronics.stackexchange.com/questions/95140/purpose-of-the-diode-and-capacitor-in-this-motor-circuit)
* [How diodes protect H-bridge DC motor driver?](https://electronics.stackexchange.com/questions/80137/how-diodes-protect-h-bridge-dc-motor-driver)
* [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/overview)
* [ARDUINO MOTOR GUIDE - 6 ARDUINO PROJECTS WITH A SPIN](https://www.circuito.io/blog/arduino-motor-guide/)

## Development for

* used for validation in ESP [voluptuous](http://alecthomas.github.io/voluptuous/docs/_build/html/modules.html) and [functions](https://github.com/alecthomas/voluptuous#validation-functions)
* based on [FormEncode Validation](https://www.formencode.org/en/latest/Validator.html)

## Pi Pico

* [Using ESPHome on the Raspberry Pi Pico W and other RP2040 microcontroller boards](https://koen.vervloesem.eu/blog/using-esphome-on-the-raspberry-pi-pico-w-and-other-rp2040-microcontroller-boards/)
* [Rpi pico w onboard temperature sensor and onboard led](https://community.home-assistant.io/t/rpi-pico-w-onboard-temperature-sensor-and-onboard-led/564904/5)

## ZigBee

* [How to Transform a RaspberryPi Into a Universal Zigbee and Z-Wave Bridge](https://hackernoon.com/how-to-transform-a-raspberrypi-into-a-universal-zigbee-and-z-wave-bridge-xy1ay3ymz) including information about z-wave vs zigbee
search for `CC2531` on amazon. See [Sniff Zigbee](https://www.zigbee2mqtt.io/advanced/zigbee/04_sniff_zigbee_traffic.html) and [alternative flashing](https://www.zigbee2mqtt.io/guide/adapters/flashing/alternative_flashing_methods.html)

* [cc2530 information](https://www.ti.com/product/CC2530) TI recommends "the ZCP 3.0 compliant CC26x2/CC13x2 family" the cheaper development board is LAUNCHXL-CC26X2R1, about £45 the similar LAUNCHXL-CC2650 is a bit cheaper. Cheap modules from [EBYTE E18-MS1-PCB](https://zigbee.blakadder.com/assets/files/E18-MS1-PCB_Usermanual_EN_v1.1.pdf) [Firmware for these devices](https://ptvo.info/faq/) someone built a mini PCB for it [Z1-Mini](https://gio-dot.github.io/Z1-Mini/) with a cookbook. Someone else build [ZigUNO shield](https://www.tindie.com/products/mind/ziguno/) with the [design files here](https://github.com/xyzroe/ZigUNO/tree/main/2530_v1) a [set of projects using this including design files](https://github.com/diyruz) little development board [design files suitable for jlcpcb](https://github.com/nicolalandro/E-18_pcb_board/tree/main) needs [TI provided sw development kit](https://www.ti.com/tool/download/SIMPLELINK-CC13X2-26X2-SDK/5.10.00.48) with their own [IDE](https://www.ti.com/tool/CCSTUDIO?keyMatch=CODE%20COMPOSER%20STUDIO) seems like it gets complicated and expensive pretty quickly [Zigbee CC2530](https://community.home-assistant.io/t/zigbee-cc2530/425998/11)

* [Flashing a CC2530 + CC2591 Zigbee Module with a Raspberry Pi](https://www.marrold.co.uk/2019/12/flashing-cc2530-cc2591-zigbee-module.html) using [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt)
