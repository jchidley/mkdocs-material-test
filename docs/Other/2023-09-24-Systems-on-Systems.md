---
date: "2023-09-24"
title: "Systems-on-Systems"
---
<!-- markdownlint-disable MD025 -->
# Systems-on-Systems
<!-- markdownlint-enable MD025 -->

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

<!-- markdownlint-disable MD034 -->
https://github.com/dorssel/usbipd-win
<!-- markdownlint-enable MD034 -->

```cmd
winget install usbipd
```

<!-- markdownlint-disable MD034 -->
https://github.com/dorssel/usbipd-win/wiki/WSL-support
<!-- markdownlint-enable MD034 -->

```bash
sudo usermod -a -G plugdev jackc # or other groups users
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

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
