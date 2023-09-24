---
date: "2023-09-24"
title: "Systems-on-Systems"
---
<!-- markdownlint-disable MD025 -->
# Systems-on-Systems
<!-- markdownlint-enable MD025 -->

## Import any Linux distribution to use with WSL

## Custom Linux for WSL

[Creating a Custom Linux Distribution for WSL](https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro)

```PS
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss" -Recurse | findstr BasePath
get-ChildItem C:\Users\jackc\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\ext4.vhdx | Select-Object @{Name='Size'; Expression={[int]($_.Length / 1MB)}}
```

```PS
dir \\wsl$\distribution-name
```

### WSL

* [Awesome-WSL: Awesome list dedicated to Windows Subsystem for Linux](https://github.com/sirredbeard/Awesome-WSL#10-gui-apps)
* [How to add second WSL2 Ubuntu distro](https://superuser.com/questions/1515246/how-to-add-second-wsl2-ubuntu-distro-fresh-install)
* [ubuntu images](https://cloud-images.ubuntu.com/wsl/)
* [How to change default user in WSL Ubuntu bash on Windows 10](https://askubuntu.com/questions/816732/how-to-change-default-user-in-wsl-ubuntu-bash-on-windows-10)
* [WSL - Connect USB devices](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
* [usbipd-win](https://github.com/dorssel/usbipd-win)
 
## Alpine WSL

[Alpine WSL GitHub](https://github.com/agowa338/WSL-DistroLauncher-Alpine)

To allow installation of packages
`Alpine.exe config --default-user root`

## Putty

I suggest that you [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to test out the connection on the Windows side.

On Windows run the "Device Manager" and expand the Ports (COM & LPT) section. Note the COM port number for the Pico; on my system it's labelled "USB Serial Device (COM7)".

Open PuTTY, select the Serial connection type and enter the COM7 (see above) in the Serial line box. Set the Speed to 115200 and click on the Open button. A window should open that repetively prints "Hello, World!".

## USB on WSL

Now it's time to deal with the WSL side of things.

https://github.com/dorssel/usbipd-win

```cmd
winget install usbipd
```

https://github.com/dorssel/usbipd-win/wiki/WSL-support

```ubuntu
sudo apt install linux-tools-virtual hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip | tail -n1` 20
```

```cmd
usbipd wsl list
# look for Picoprobe entry, like this:
# 1-2    2e8a:0004  USB Serial Device (COM5), Picoprobe
# you might not need the "--distribution ubuntu" part if you only have one WSL distribution installed
usbipd wsl attach --busid 1-2 --distribution ubuntu
```

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
