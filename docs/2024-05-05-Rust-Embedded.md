---
date: "2024-05-05"
title: "Rust Embedded"
tags:
  - rust
  - embedded
  - raspberry-pi
  - microcontrollers
  - testing
---
<!-- markdownlint-disable MD025 -->
# rust Embedded
<!-- markdownlint-enable MD025 -->

## Update from 30/12/24

[This is the website for Jonathan 'theJPster' Pallant](https://thejpster.org.uk/) he does rust embedded stuff, like this [Neotron Pico](https://neotron-compute.github.io/Neotron-Book/neotron_pico.html)

[A fast and flexible allocator for no_std and WebAssembly](https://crates.io/crates/talc)

## Previously

[embassy-template](https://github.com/lulf/embassy-template) "Simple template to generate a embassy project for a few common boards. Make sure you've run cargo install cargo-generate before using."

[defmt book](https://defmt.ferrous-systems.com/introduction) "defmt ("de format", short for "deferred formatting") is a highly efficient logging framework that targets resource-constrained devices, like microcontrollers."

## Operating System development tutorials in Rust on the Raspberry Pi

[rust-raspberrypi-OS-tutorials](https://github.com/rust-embedded/rust-raspberrypi-OS-tutorials)

## Introduction

The guy that built JeeLabs's stuff, for exampe JeeNode [JC's Logbook](https://jc.wippler.nl/posts/)
"How do you make sure that all “readings” get logged, yet still retain the ability to adjust and extend the underlying database and software?" [The logic of data logging](https://web.archive.org/web/20170730145913/http://jeelabs.org/2009/03/22/the-logic-of-data-logging/index.html)

The improved version of JeeNode's communications chip was done by [Low Power Lab](https://lowpowerlab.com/)
To measure very low voltages or currents [CurrentRanger](https://lowpowerlab.com/shop/product/152)

see also [Pi Pico](2023-11-05-Pi-Pico.md)

* [Embassy is a project to make async/await a first-class option for embedded development.](https://embassy.dev/book/)
* [Embedded Rust & Embassy: GPIO Button Controlled Blinking](https://dev.to/theembeddedrustacean/embedded-rust-embassy-gpio-button-controlled-blinking-3ee6)

* [Writing an OS in Rust ](https://os.phil-opp.com/)
* [Discover the world of microcontrollers through Rust!](https://docs.rust-embedded.org/discovery/microbit/index.html)
* [MicroBit Schematic](https://github.com/microbit-foundation/microbit-v2-hardware/blob/main/V2.00/MicroBit_V2.0.0_S_schematic.PDF)
* [Embedded Rust documentation](https://docs.rust-embedded.org/)

* [Get-PnpDevice = Returns information about PnP devices.](https://learn.microsoft.com/en-us/powershell/module/pnpdevice/get-pnpdevice?view=windowsserver2022-ps)

* [The Drogue IoT project aims to bring together data and users in an Internet of Things world.](https://github.com/drogue-iot)
* [Embedded development](https://lib.rs/embedded?sort=popular)
* [rust-mqtt](https://lib.rs/crates/rust-mqtt)

* [Introduction to Rust programming on bare metal hardware by Mike Kefeder - Rust Zürisee March 2023](https://www.youtube.com/watch?v=KECu_piSM5s)
* [The Embedded Rust ESP Development Ecosystem](https://dev.to/apollolabsbin/embedded-rust-the-esp-development-ecosystem-5478)
(Embedded Developer)[https://blog.mark-stevens.co.uk/]

# Embedded HALs

There appear to be at least 2 completely different HALs/APIs/ecosystems for supporting Raspberry Pi Picos. 

* [Embassy RP HAL implements both blocking and async APIs for many peripherals](https://github.com/embassy-rs/embassy/tree/main/embassy-rp)
* [Rust support for the "Raspberry Silicon" family of microcontrollers](https://github.com/rp-rs/rp-hal)

These are not compatible, see [Embassy-RP and RP2040-hal Compatibility?](https://github.com/embassy-rs/embassy/issues/3180) and [Embassy-RP and RP2040-hal Compatibility?](https://github.com/rp-rs/rp-hal/issues/816)

## rust-analyzer

[helix - Language Server Configurations](https://github.com/helix-editor/helix/wiki/Language-Server-Configurations#rust) :"Everything under the rust-analyzer key goes under language-server.rust-analyzer.config key in helix" 

From [rust-analyzer manual](https://rust-analyzer.github.io/manual.html)

"rust-analyzer does not require Cargo. However, if you use some other build system, you’ll have to describe the structure of your project for rust-analyzer in the rust-project.json format:"

## Debugging

[rtt](https://docs.rs/rtt-target/latest/rtt_target/)

only appears in debug compilation. There's also a function to send information back "Reading".

```
use rtt_target::{debug_rtt_init_print, debug_rprintln};

fn main() -> ! {
    debug_rtt_init_print!(); // nop in --release
    loop {
        debug_rprintln!("Hello, world!"); // not present in --release
    }
}
```

[defmt](https://defmt.ferrous-systems.com/) ("de format", short for "deferred formatting") is a highly efficient logging framework that targets resource-constrained devices, like microcontrollers.

### rust toolchain override causes rust-analyzer language server to exit.

[Github issue raised](https://github.com/helix-editor/helix/issues/11612)

[rust toolchain override](https://rust-lang.github.io/rustup/overrides.html) causes rust-analyzer Language server to exit.

`rustup toolchain list`:

```
stable-x86_64-pc-windows-msvc (default)
1.80-x86_64-pc-windows-msvc (override)
```

`helix.log`:

```
2024-08-31T14:20:03.024 helix_lsp::transport [ERROR] rust-analyzer err <- "error: Unknown binary 'rust-analyzer.exe' in official toolchain '1.80-x86_64-pc-windows-msvc'.\n"
2024-08-31T14:20:03.074 helix_lsp::transport [ERROR] rust-analyzer err: <- StreamClosed
2024-08-31T14:20:03.074 helix_lsp [ERROR] failed to initialize language server: server closed the stream
```


`rust-toolchain.toml`:

```
[toolchain]
channel = "1.80"
components = [ "rust-src", "rustfmt", "llvm-tools" ]
targets = [
    "thumbv7em-none-eabi",
    "thumbv7m-none-eabi",
    "thumbv6m-none-eabi",
    "thumbv7em-none-eabihf",
    "thumbv8m.main-none-eabihf",
    "riscv32imac-unknown-none-elf",
    "wasm32-unknown-unknown",
]
```

VS Code works fine with this configuration, helix doesn't.

#### Mitigation

Start helix from a directory where the override isn't in effect to edit the desired file.

## Embassy HALs

Discovery f0 has interesting peripherals but these need to be added (LD4 for an LED is the most prosaic)

(Note: search command history with PowerShell `rg probe-rs $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine`)

For ST chips, might need to update firmware using [STSW-LINK007](https://www.st.com/en/development-tools/stsw-link007.html)

need to adjust `.\.cargo\config.toml` runner command (find the chip with `probe-rs chip info nrf528` and might need to add the `--probe` parameter too with the USB ID)

and flavours in `Cargo.toml` (e.g. for STM32 see `https://github.com/embassy-rs/embassy/blob/main/embassy-stm32/Cargo.toml`)

microbit v2 [microbit-bsp](https://github.com/lulf/microbit-bsp.git) had to add ""--probe" argument (find using `probe-rs info`). Also adapted the `embassy\examples\nrf52840` but I'm not sure the bsp is complete - compiles and is loaded but doesn't seem to do anything.

### Works

```
rp2040
Cores (2):
    - core0 (Armv6m)
    - core1 (Armv6m)
RAM: 0x20000000..0x20042000 (264.00 KiB)
RAM: 0x21000000..0x21010000 (64.00 KiB)
RAM: 0x21010000..0x21020000 (64.00 KiB)
RAM: 0x21020000..0x21030000 (64.00 KiB)
RAM: 0x21030000..0x21040000 (64.00 KiB)
NVM: 0x10000000..0x18000000 (128.00 MiB)
```

```
STM32F303RETx
Cores (1):
    - main (Armv7em)
RAM: 0x20000000..0x20010000 (64.00 KiB)
NVM: 0x08000000..0x08080000 (512.00 KiB)
```

```
nRF52833_xxAA
Cores (1):
    - main (Armv7em)
RAM: 0x20000000..0x20020000 (128.00 KiB)
RAM: 0x00800000..0x00820000 (128.00 KiB)
NVM: 0x00000000..0x00080000 (512.00 KiB)
NVM: 0x10001000..0x10002000 (4.00 KiB)
```

```
STM32F072RBTx
Cores (1):
    - main (Armv6m)
RAM: 0x20000000..0x20004000 (16.00 KiB)
NVM: 0x08000000..0x08020000 (128.00 KiB)
```

```
STM32F030R8Tx
Cores (1):
    - main (Armv6m)
RAM: 0x20000000..0x20002000 (8.00 KiB)
NVM: 0x08000000..0x08010000 (64.00 KiB)
```

```
STM32F051R8Tx
Cores (1):
    - main (Armv6m)
RAM: 0x20000000..0x20002000 (8.00 KiB)
NVM: 0x08000000..0x08010000 (64.00 KiB)
```

blinky in debug will not fit, but --release will

```
stm32f302r8tx
Cores (1):
    - main (Armv7em)
RAM: 0x20000000..0x20004000 (16.00 KiB)
NVM: 0x08000000..0x08010000 (64.00 KiB)
```

blinky --release works, --debug won't

```
stm32l031k6tx
Cores (1):
    - main (Armv6m)
RAM: 0x20000000..0x20002000 (8.00 KiB)
NVM: 0x08000000..0x08008000 (32.00 KiB)
```

### STM32 flash too small

blinky --release overflowed:

```
= note: rust-lld: error: section '.bss' will not fit in region 'RAM': overflowed by 2388 bytes
rust-lld: error: section '.uninit' will not fit in region 'RAM': overflowed by 3412 bytes
```

```
stm32l011k4tx
Cores (1):
    - main (Armv6m)
RAM: 0x20000000..0x20000800 (2.00 KiB)
NVM: 0x08000000..0x08004000 (16.00 KiB)
```

## Testing

Testing embedded Rust is tricky because `cargo test` uses `std` which doesn't exist for embedded targets.

### Test-Driven Development with Mocking

[Test driven embedded rust](https://hackaday.io/page/21907-test-driven-embedded-rust-development-tutorial) — TDD is especially useful for embedded systems, as testing on target hardware is significantly more difficult than host testing. Uses [mockall - a powerful mock object library for Rust](https://docs.rs/mockall/latest/mockall/#user-guide).

Comment out `target = "thumbv7em-none-eabihf"` in the `[build]` section of `.cargo/config.toml`, so you will need to `cargo build --release --target=thumbv7em-none-eabihf` for cargo.

Add at the top of source files:

```rust
#![cfg_attr(not(test), no_main)]
#![cfg_attr(not(test), no_std)]

#[cfg(not(test))]
use panic_halt as _;
```

Need to use [mockall](https://docs.rs/mockall/latest/mockall/) — add `[dev-dependencies] mockall = "0.13.1"`

See also [Mocking in Rust: Mockall and alternatives](https://blog.logrocket.com/mocking-rust-mockall-alternatives/) and [Rust Unit Testing - Mockall Crate](https://www.youtube.com/watch?v=zp6HuZ56Cl4)

### no_std Testing Challenges

One way is to use [custom_test_frameworks](https://rust-lang.github.io/rfcs/2318-custom-test-frameworks.html) as noted in [The Rust Unstable Book](https://doc.rust-lang.org/unstable-book/language-features/custom-test-frameworks.html). There's a long blog entry on [testing](https://os.phil-opp.com/testing/) in "Writing an OS in Rust" by Philipp Oppermann.

Other sources: [How to test code when #![no_std] is set](https://users.rust-lang.org/t/how-to-test-code-when-no-std-is-set/93180), [How do I test crates with #![no_std]?](https://stackoverflow.com/questions/28185854/how-do-i-test-crates-with-no-std), [Testing for no_std compatibility in Rust crates](https://blog.dbrgn.ch/2019/12/24/testing-for-no-std-compatibility/) and [Nine Rules for Running Rust on Embedded Systems](https://towardsdatascience.com/nine-rules-for-running-rust-on-embedded-systems-b0c247ee877e)

Either include `#![cfg_attr(not(test), no_std)]` at the top of the file or add:

```rust
#[cfg(test)]
mod tests {
    extern crate std;
}
```

### Nine Rules Summary

* **Rule 1:** Confirm that your project works with WASM WASI and WASM in the Browser.

```bash
cargo test --target wasm32-wasip1
cargo test --target wasm32-unknown-unknown
```

* **Rule 2:** Use target thumbv7m-none-eabi and cargo tree to identify and fix dependencies incompatible with no_std.

```bash
rustup target add thumbv7m-none-eabi
cargo check --target thumbv7m-none-eabi
# then
cargo tree --edges no-dev --format "{p} {f}"
```

* **Rule 3:** Mark main (non-test) code no_std and alloc. Replace std:: with core:: and alloc::.
* **Rule 4:** Use Cargo features to let your main code use std optionally for file-related (etc.) functions.
* **Rule 5:** Understand why test code always uses the standard library.

```bash
# DOES NOT TEST `no_std`
cargo test --no-default-features
```

"Functions from std that are unavailable in a true no_std environment will still be accessible during testing."

```rust
#![cfg(test)]
// imports required for testing
use std::prelude::v1::*;
use std::{format, print, println, vec};
```

* **Rule 6:** Create a simple embedded test project. Run it with QEMU.

## From C to Rust

* [C2Rust](https://github.com/immunant/c2rust?tab=readme-ov-file)
* [Citrus: Convert C to Rust](https://gitlab.com/citrus-rs/citrus)
* [Lessons learned porting C++ to rust](https://www.youtube.com/watch?v=kcMAiTg5j1w)

### c2rust

For Arduino sketches, this consists of:

1. Compile using arduino-cli
2. cd to build directory `cd /tmp/arduino/sketches/EA070D50AE3989211800C04360BDAE60` for example
3. inspect `compile_commands.json` using `bat compile_commands.json -r 1:35` for example
4. rename .cpp to .c if required

Then rounds of:

1. `c2rust transpile blink.c -- -I/home/jackc/.arduino15/packages/arduino/hardware/avr/1.8.6/cores/arduino`
2. remove current rust output e.g. `rm blink.rs`
3. Find missing includes: `fd pgmspace.h ~ -H` for example
4. include them in new commmand.

If you'd prefer to avoid `arduino-cli` then [PlatformIO Core CLI](https://docs.platformio.org/en/latest/core/installation/index.html) is an alternative.

### Pi Pico

* [Raspberry Pi Pico Lecture 14: Introducing PIO](https://www.youtube.com/watch?v=BVdaw56Ln8s&list=PLDqMkB5cbBA5oDg8VXM110GKc-CmvUqEZ&index=14)
* [Raspberry Pico: Programming with PIO State Machines](https://dev.to/admantium/raspberry-pico-programming-with-pio-state-machines-1gbg)
* [A Practical Look at PIO on the Raspberry Pi Pico](https://dev.to/blues/a-practical-look-at-pio-on-the-raspberry-pi-pico-50j8)

### rust

[Embassy pio module embassy_rp::pio](https://docs.embassy.dev/embassy-rp/git/rp2040/pio/index.html)

[pio-rs](https://github.com/rp-rs/pio-rs) note: "you can call pio::assembler::new() and construct a pio program using the 'builder pattern' - effectively you are compiling a pio program at run-time on the rp2040 itself!"

Note that embassy includes it's own Pico specific HALs, etc

[pio-rs](https://github.com/rp-rs/pio-rs)


