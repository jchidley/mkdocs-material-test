---
date: "2023-09-09"
title: " Picocomputer"
---
<!-- markdownlint-disable MD025 -->
# Picocomputer
<!-- markdownlint-enable MD025 -->

## Install Raspberry Pi Pico

https://learn.pimoroni.com/article/pico-development-using-wsl

after you've made the various standard Raspberry Pi examples, I suggest that you copy over the hello_world/usb example.

Now it's time to install the necessary software for the usb exmple to test out serial communication. I suggest that you [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to test out the connection on the Windows side.

On Windows run the "Device Manager" and expand the Ports (COM & LPT) section. Note the COM port number for the Pico; on my system it's labelled "USB Serial Device (COM7)".

Open PuTTY, select the Serial connection type and enter the COM7 (see above) in the Serial line box. Set the Speed to 115200 and click on the Open button. A window should open that repetively prints "Hello, World!".

Now it's time to deal with the WSL side of things.

see [2023-09-24-Systems-on-Systems.md](2023-09-24-Systems-on-Systems.md) for `usbipd`

### openocd

```ubuntu
$ sudo apt install automake autoconf build-essential texinfo libtool libftdi-dev libusb-1.0-0-dev
sudo apt install pkg-config # missing on my WSL ubuntu
$ git clone https://github.com/raspberrypi/openocd.git --branch rp2040-v0.12.0 --depth=1 --no-single-branch
cd openocd
./bootstrap
./configure
make -j8
sudo make install
```


## Software Installation

I recommend using [Scoop](https://github.com/ScoopInstaller/Scoop) 
```cmd
iwr -useb get.scoop.sh | iex
scoop install cmake make msys2 
msys2
pacman -Syyu
```

goto https://cc65.github.io/ 

click on *Windows Snapshot* link at the bottom of the page, this will take you to Sourceforge and start the download after a short delay.

Extract the downloaded file into a suitalble directory (I chose "C:\cc65")

The add "C:\cc65\bin" to the user's path environmental variable. Add other directories as needed.

Install Visual Studio Code from its usual page. Open up the project folder that you previously cloned from github.

## Links

<!-- markdownlint-disable MD034 -->

<!-- markdownlint-enable MD034 -->
