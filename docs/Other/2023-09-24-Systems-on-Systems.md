---
date: "2023-09-24"
title: "Systems-on-Systems"
---
<!-- markdownlint-disable MD025 -->
# Systems-on-Systems
<!-- markdownlint-enable MD025 -->

## Linux Kernel Building on WSL 2

[Building your own WSL 2 kernel with additional drivers](https://github.com/dorssel/usbipd-win/wiki/WSL-support#building-your-own-wsl-2-kernel-with-additional-drivers)
"Recent versions of Windows running WSL kernel 5.10.60.1 or later already include support for common scenarios like USB-to-serial adapters and flashing embedded development boards. Only if you require special drivers will you need to build your own kernel for WSL 2."

```cmd
wsl --update
# Export current distribution to be able to fall back if something goes wrong.
wsl --export <current-distro> <temporary-path>\wsl2-usbip.tar
# Import new distribution with current distribution as base.
wsl --import wsl2-usbip <install-path> <temporary-path>\wsl2-usbip.tar
# Run new distribution.
wsl --distribution wsl2-usbip --user <user>
# upgrade it
sudo apt update &&  sudo apt -y full-upgrade
# Install prerequisites.
sudo apt install build-essential flex bison libssl-dev libelf-dev libncurses-dev autoconf libudev-dev libtool
# Clone kernel that matches WSL version. To find the version you can run.
uname -r
# Clone the kernel repo, then checkout the branch/tag that matches your kernel version
git clone https://github.com/microsoft/WSL2-Linux-Kernel.git
cd WSL2-Linux-Kernel
git checkout linux-msft-wsl-5.10.43.3
# Copy current configuration file.
cp /proc/config.gz config.gz
gunzip config.gz
mv config .config
# add features
sudo make menuconfig
# number of processors
getconf _NPROCESSORS_ONLN
# substitute 8 below for the number from above
sudo make -j 8 && sudo make modules_install -j 8 && sudo make install -j 8
cp arch/x86/boot/bzImage /mnt/c/Users/<user>/usbip-bzImage
# Create a `.wslconfig file` on `/mnt/c/Users/<user>/` and add a reference to the created image with the following.
[wsl2]
kernel=c:\\users\\<user>\\usbip-bzImage
```

## WSL

[How to locate the .vhdx file and disk path for your Linux distribution](https://learn.microsoft.com/en-us/windows/wsl/disk-space#how-to-locate-the-vhdx-file-and-disk-path-for-your-linux-distribution)

Finding

```PowerShell
Foreach ($i in Get-ChildItem -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss) {write-host $i.GetValue("BasePath")}
# Get-ChildItem -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | foreach-object {write-host $_.GetValue("BasePath")}
```

Exporting

```PowerShell
wsl --export --vhd Alpine D:\WindowsBackup\WSL2\Alpine.vhdx
```

## Virtual Machines

[Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server)

```PowerShell
Get-VM | Export-VM -Path D:\WindowsBackup\
```

## Import any Linux distribution to use with WSL

## Custom Linux for WSL

[Import any Linux distribution to use with WSL](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro)

### Here Stings, Environment

Pass a command to WSL without PowerShell expanding it first

```PS
@'
echo $SHELL
'@ | wsl -d U3 --
```

Expand the string in Powershell then send it to WSL

```PS
@"
echo $ENV:OS
"@ | wsl -d U3 --
```

Boom!

```PS
@"
echo $ENV:OS `$SHELL
"@ | wsl -d U3 --
```

wsl is started in the current (windows) directory, and windows files appear in Linux with 777 permissions, so this works

```PS
 @'
echo this system is $(uname)
'@ | > .\new.sh ; wsl -d U3 ./new.sh
```

or this:

```PS
$tmp = New-TemporaryFile
@"
echo $env:os wrote it, `$(uname) is executing it
"@ | out-file -filepath $tmp ; type $tmp | wsl -d U3 sh --
```

```PS
$tmpfile = New-TemporaryFile
@"
wslpath '$tmpfile'
"@ | wsl -d U3
```

also can access WSL from \\wsl$\distribution

[about_Quoting_Rules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-7.3)

[about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3)

### Ubuntu

```PS
# wsl --unregister Gentoo
# download the file to <FileName>
mkdir -p <InstallLocation>
wsl --import <Distro> <InstallLocation> <FileName>
wsl -d <Distro>
```

```bash
cat << EOF > /etc/wsl.conf
[boot]
systemd=true
[user]
default=jackc
EOF
useradd -G sudo -m -s /bin/bash jackc
passwd jackc
sed -E -i 's|^\s*(%sudo.*\s+)(ALL)\s*$|\1NOPASSWD:\2|' /etc/sudoers
# EDITOR=vi visudo
# NOPASSWD:ALL
sudo apt update && sudo apt -y full-upgrade
```

```PS
wsl -t U3
wsl -d U3
```

## USB on WSL

Now it's time to deal with the WSL side of things.

[usbipd-win](https://github.com/dorssel/usbipd-win)
[usbipd-win on WSL 2](https://github.com/dorssel/usbipd-win#wsl-2)
[WSL support](https://github.com/dorssel/usbipd-win/wiki/WSL-support)

```cmd
winget install usbipd
usbipd list
usbipd bind --busid 4-4 # or "4-4" for another, "Shared" survives reboot
# --auto-attach (also '-a') runs in a loop to reattach, so blocks shell.
usbipd attach --wsl --auto-attach --busid 4-4
```

### udev

On WSL, this will probably be required

For [probe-rs](https://probe.rs/docs/getting-started/probe-setup/#linux%3A-udev-rules)'s advice, see below:

```
Linux: udev rules
By default, the debug probes are only accessible by users with root privileges on Linux based systems. It is recommend to use appropriate udev rules to allow users without root privileges access to the debug probes as well.

Download the rules file and place it in /etc/udev/rules.d.
Run udevadm control --reload to ensure the new rules are used.
Run udevadm trigger to ensure the new rules are applied to already added devices.
If you're still unable to access the debug probes after following these steps, try adding your user to the plugdev group.

[^1]: The file needs to have an initial number lower than 73, otherwise the udev rules do not get applied properly. See this Github discussion for more information.

If you are using WSL, you may need to enable the udev service. To check if the service is running, run service udev status. If the service is not started, edit /etc/wsl.conf (with sudo) and make sure the following is included:

[boot]
command="service udev start"
```

From the [usbipd wiki](https://github.com/dorssel/usbipd-win/wiki/WSL-support#udev)'s entry about udev:  "using embedded devices with openocd, copy `share/openocd/contrib60-openocd.rules` to the `/etc/udev/rules.d folder`"

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

Open PuTTY, select the Serial connection type and enter the COM7 (see above) in the Serial line box. Set the Speed to 115200 and click on the Open button. A window should open that repetitively prints "Hello, World!".

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
