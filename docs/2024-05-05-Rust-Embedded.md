---
date: "2024-05-05"
title: "rust-Embedded"
---
<!-- markdownlint-disable MD025 -->
# rust Embedded
<!-- markdownlint-enable MD025 -->

## Introduction

see also [Pi Pico](2023-11-05-Pi-Pico.md)

* [Embassy is a project to make async/await a first-class option for embedded development.](https://embassy.dev/book/dev/index.html)
* [Embedded Rust & Embassy: GPIO Button Controlled Blinking](https://dev.to/theembeddedrustacean/embedded-rust-embassy-gpio-button-controlled-blinking-3ee6)

* [Writing an OS in Rust ](https://os.phil-opp.com/)
* [Discover the world of microcontrollers through Rust!](https://docs.rust-embedded.org/discovery/microbit/index.html)
* [Embedded Rust documentation](https://docs.rust-embedded.org/)

* [Get-PnpDevice = Returns information about PnP devices.](https://learn.microsoft.com/en-us/powershell/module/pnpdevice/get-pnpdevice?view=windowsserver2022-ps)

* [The Drogue IoT project aims to bring together data and users in an Internet of Things world.](https://github.com/drogue-iot)
* [Embedded development](https://lib.rs/embedded?sort=popular)
* [rust-mqtt](https://lib.rs/crates/rust-mqtt)

* [Introduction to Rust programming on bare metal hardware by Mike Kefeder - Rust Zürisee March 2023](https://www.youtube.com/watch?v=KECu_piSM5s)
* [The Embedded Rust ESP Development Ecosystem](https://dev.to/apollolabsbin/embedded-rust-the-esp-development-ecosystem-5478)

# Embedded HALs

There appear to be at least 2 completely different HALs/APIs/ecosystems for supporting Raspberry Pi Picos. 

* [Embassy RP HAL implements both blocking and async APIs for many peripherals](https://github.com/embassy-rs/embassy/tree/main/embassy-rp)
* [Rust support for the "Raspberry Silicon" family of microcontrollers](https://github.com/rp-rs/rp-hal)

These are not compatible, see [Embassy-RP and RP2040-hal Compatibility?](https://github.com/embassy-rs/embassy/issues/3180) and [Embassy-RP and RP2040-hal Compatibility?](https://github.com/rp-rs/rp-hal/issues/816)

## From C to Rust

* [C2Rust](https://github.com/immunant/c2rust?tab=readme-ov-file)
* [Citrus: Convert C to Rust](https://gitlab.com/citrus-rs/citrus)
* [Lessons learned porting C++ to rust](https://www.youtube.com/watch?v=kcMAiTg5j1w)

### Pi Pico

* [Raspberry Pi Pico Lecture 14: Introducing PIO](https://www.youtube.com/watch?v=BVdaw56Ln8s&list=PLDqMkB5cbBA5oDg8VXM110GKc-CmvUqEZ&index=14)
* [Raspberry Pico: Programming with PIO State Machines](https://dev.to/admantium/raspberry-pico-programming-with-pio-state-machines-1gbg)
* [A Practical Look at PIO on the Raspberry Pi Pico](https://dev.to/blues/a-practical-look-at-pio-on-the-raspberry-pi-pico-50j8)

### rust

[pio-rs](https://github.com/rp-rs/pio-rs) note: "you can call pio::assembler::new() and construct a pio program using the 'builder pattern' - effectively you are compiling a pio program at run-time on the rp2040 itself!"

Note that embassy includes it's own Pico specific HALs, etc

[pio-rs](https://github.com/rp-rs/pio-rs)

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
