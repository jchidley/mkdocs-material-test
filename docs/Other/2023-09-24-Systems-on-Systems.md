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

```sh
# cmd
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

```sh
# PowerShell
Foreach ($i in Get-ChildItem -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss) {write-host $i.GetValue("BasePath")}
# Get-ChildItem -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | foreach-object {write-host $_.GetValue("BasePath")}
```

Exporting

```sh
# PowerShell
wsl --export --vhd Alpine D:\WindowsBackup\WSL2\Alpine.vhdx
```

## Virtual Machines

[Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server)

```sh
# PowerShell
Get-VM | Export-VM -Path D:\WindowsBackup\
```

## Custom Linux for WSL

[Import any Linux distribution to use with WSL](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro)

### Here Stings, Environment, heredoc

### Linux

[Here Documents and Here Strings](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Here-Documents)

This type of redirection instructs the shell to read input from the current source until a line containing only word (with no trailing blanks) is seen. All of the lines read up to that point are then used as the standard input (or file descriptor n if n is specified) for a command.

The format of here-documents is:

```sh
[n]<<[-]word
        here-document
delimiter
```

No parameter and variable expansion, command substitution, arithmetic expansion, or filename expansion is performed on word. If any part of word is quoted, the delimiter is the result of quote removal on word, and the lines in the here-document are not expanded. If word is unquoted, all lines of the here-document are subjected to parameter expansion, command substitution, and arithmetic expansion, the character sequence \newline is ignored, and ‘\’ must be used to quote the characters ‘\’, ‘$’, and ‘`’.

If the redirection operator is ‘<<-’, then all leading tab characters are stripped from input lines and the line containing delimiter. This allows here-documents within shell scripts to be indented in a natural fashion.

3.6.7 Here Strings
A variant of here documents, the format is:

```bash
[n]<<< word
```

The word undergoes tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal. Filename expansion and word splitting are not performed. The result is supplied as a single string, with a newline appended, to the command on its standard input (or file descriptor n if n is specified).

[https://thelinuxcode.com/bash-heredoc-tutorial/](https://thelinuxcode.com/bash-heredoc-tutorial/)

```bash
# replaces l with e
cat << EOF |  sed 's/l/e/g'
Hello
World
EOF
# <<- strip tabs, I believe that my editor is replacing the tabs with spaces
cat <<- EOF
  Line with a leading tab.
EOF
# no parameter expansion
cat << "EOF" #'EOF' also works
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
# output to file, expands parameters
at << EOF > file.txt
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
OUTFILE=$(mktemp) # temporary file
# normally tee echos the output
sudo tee "$OUTFILE" > /dev/null <<'EOF'
foo
bar
EOF
# using dd
sudo dd of="$OUTFILE" <<EOF
foo
bar
EOF
# This starts a sub-shell under sudo, and opens $OUTFILE from that more privileged
# subprocess, and runs cat (as yet another privileged subprocess). Meanwhile, the
# (less privileged) parent process pipes the here-document to the sudo subprocess.
sudo bash -c "cat > $OUTFILE" << EOF
#!/bin/bash
#? [ ] / \ = + < > : ; " , * | 
#/ ? < > \ : * | ”
#Filename="z:"${$winFn//\//\\}
echo "This is a generated shell script."
App='eval wine "C:\Program Files\foxit\Foxit Reader.exe" "'$winFn'"'
$App
EOF
```

Pass a command to WSL without PowerShell expanding it first

```sh
# PowerShell
@'
echo $SHELL
'@ | wsl -d U3 --
# Expand the string in Powershell then send it to WSL
@"
echo $ENV:OS
"@ | wsl -d U3 --
# send it to linux
@"
echo $ENV:OS `$SHELL
"@ | wsl -d U3 --
```

wsl is started in the current (windows) directory, and windows files appear in Linux with 777 permissions, so this works

```sh
# PowerShell
 @'
echo this system is $(uname)
'@ | > .\new.sh ; wsl -d U3 ./new.sh
# or this:
$tmp = New-TemporaryFile
@"
echo $env:os wrote it, `$(uname) is executing it
"@ | out-file -filepath $tmp ; type $tmp | wsl -d U3 sh --
```

temporary file

```sh
# PowerShell
$tmpfile = New-TemporaryFile
@"
wslpath '$tmpfile'
"@ | wsl -d U3
```

also can access WSL from \\wsl$\distribution

[about_Quoting_Rules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-7.3)

[about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3)

### Ubuntu

```sh
# PowerShell
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

```sh
# PowerShell
wsl -t U3
wsl -d U3
```

## USB on WSL

Now it's time to deal with the WSL side of things.

[usbipd-win](https://github.com/dorssel/usbipd-win)
[usbipd-win on WSL 2](https://github.com/dorssel/usbipd-win#wsl-2)
[WSL support](https://github.com/dorssel/usbipd-win/wiki/WSL-support)

```sh
# PowerShell
winget install usbipd
usbipd list
usbipd bind --busid 4-4 # or "4-4" for another, "Shared" survives reboot
# --auto-attach (also '-a') runs in a loop to reattach, so blocks shell.
usbipd attach --wsl --auto-attach --busid 4-4
```

### udev

On WSL, this will probably be required

For [probe-rs](https://probe.rs/docs/getting-started/probe-setup/#linux%3A-udev-rules)'s advice, see below:

Linux: udev rules
By default, the debug probes are only accessible by users with root privileges on Linux based systems. It is recommend to use appropriate udev rules to allow users without root privileges access to the debug probes as well.

Download the rules file and place it in /etc/udev/rules.d.
Run udevadm control --reload to ensure the new rules are used.
Run udevadm trigger to ensure the new rules are applied to already added devices.
If you're still unable to access the debug probes after following these steps, try adding your user to the plugdev group.

[^1]: The file needs to have an initial number lower than 73, otherwise the udev rules do not get applied properly. See this Github discussion for more information.

If you are using WSL, you may need to enable the udev service. To check if the service is running, run service udev status. If the service is not started, edit /etc/wsl.conf (with sudo) and make sure the following is included:

```sh
[boot]
command="service udev start"
```

From the [usbipd wiki](https://github.com/dorssel/usbipd-win/wiki/WSL-support#udev)'s entry about udev:  "using embedded devices with openocd, copy `share/openocd/contrib60-openocd.rules` to the `/etc/udev/rules.d folder`"

```sh
# PowerShell
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss" -Recurse | findstr BasePath
get-ChildItem C:\Users\jackc\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\ext4.vhdx | Select-Object @{Name='Size'; Expression={[int]($_.Length / 1MB)}}
```

```sh
dir \\wsl$\distribution-name
```

### WSL

* [Awesome-WSL: Awesome list dedicated to Windows Subsystem for Linux](https://github.com/sirredbeard/Awesome-WSL#10-gui-apps)
* [How to add second WSL2 Ubuntu distro](https://superuser.com/questions/1515246/how-to-add-second-wsl2-ubuntu-distro-fresh-install)
* [ubuntu images](https://cloud-images.ubuntu.com/wsl/)
* [How to change default user in WSL Ubuntu bash on Windows 10](https://askubuntu.com/questions/816732/how-to-change-default-user-in-wsl-ubuntu-bash-on-windows-10)
* [WSL - Connect USB devices](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
* [usbipd-win](https://github.com/dorssel/usbipd-win)

### Alpine WSL

new process

[Build a Custom Linux Distribution for WSL](https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro)

use [alpine-chroot-install](https://github.com/alpinelinux/alpine-chroot-install) to install alpine in its own directory an an existing linux system. Run `destroy` to remove all the bindings.

[wsl.conf](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconf) which are system specific settings. see also [.wslconfig](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig) for settings for all wsl.

```sh
# PowerShell
# clean start
wsl # the host system
wsl.exe --unregister alp
rm alpine-chroot-install
rm ~/alpine.wsl.gz
/alpine/destroy -r
```

```bash
wget https://raw.githubusercontent.com/alpinelinux/alpine-chroot-install/v0.14.0/alpine-chroot-install \
    && echo 'ccbf65f85cdc351851f8ad025bb3e65bae4d5b06  alpine-chroot-install' | sha1sum -c \
    || exit 1
sudo ./alpine-chroot-install -p helix \
-p tree-sitter-javascript \
-p tree-sitter-toml \
-p tree-sitter-python \
-p tree-sitter-typescript \
-p tree-sitter-json \
-p tree-sitter-rust \
-p tree-sitter-ini \
-p tree-sitter-regex \
-p tree-sitter-css \
-p tree-sitter-c \
-p tree-sitter-bash \
-p tree-sitter-comment \
-p tree-sitter-cpp \
-p tree-sitter-html \
-p openrc \
-p docker \
-p fd \
-p bat

# unbind the various mounts for chroot: we don't want them
/alpine/destroy

sudo mkdir /alpine/usr/lib/wsl
cat << EOF | sudo tee /alpine/usr/lib/wsl/terminal-profile.json
{
  "profiles": [
    {
      "colorScheme": "Gruvbox Dark (Hard)"
    }
  ]
}
EOF

cat << EOF | sudo tee /alpine/etc/wsl-distribution.conf
# /etc/wsl-distribution.conf

[oobe]
command = /etc/oobe.sh
defaultUid = 0 # root user, can use 1000 for normal (or another number), this needs
# to match the same id used in oobe.sh
defaultName = alp #  or some other name, used in the `wsl -d` etc commands

[shortcut]
icon = /usr/lib/wsl/my-icon.ico

[windowsterminal]
ProfileTemplate = /usr/lib/wsl/terminal-profile.json
EOF

# to startup docker
cat << EOF | sudo tee /alpine/etc/oobe.sh
# /etc/oobe.sh
ln -s /etc/init.d/docker /etc/runlevels/boot/docker 
echo "run wsl.exe -t alp"
exit
EOF
sudo chmod +x /alpine/etc/oobe.sh

# seems to be required for docker
cat << EOF | sudo tee /alpine/etc/network/interfaces
# /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback
EOF

cat << EOF | sudo tee /alpine/etc/wsl.conf
# /etc/wsl.conf

[boot]
systemd=false
command = /sbin/openrc boot
# if systemd=true then WSL will try to start run `systemd` on boot.
EOF

# wsl.exe --unregister alp # this needs to be manual
cd /alpine
# if you're really worried about size, use `--best` for `gzip`
sudo tar --numeric-owner --absolute-names -c  * | gzip --fast > ~/alpine.wsl.gz
wsl.exe --install --from-file ~/alpine.wsl.gz # surprisingly fast with alpine.
```

```sh
# PowerShell
wsl.exe -d alp
```

see [OpenRC](https://wiki.alpinelinux.org/wiki/OpenRC) for some information about that. [How to enable and start services on Alpine Linux](https://www.cyberciti.biz/faq/how-to-enable-and-start-services-on-alpine-linux/) is useful but the `rc` appears to be `openrc` now. `openrc shutdown` sort of shuts down alpine but `wsl -t` actually stops it.

```sh
rc-service {service-name} restart # OR
/etc/init.d/{service-name} restart
```

[What's the difference between "Service" and "/etc/init.d/"?](https://askubuntu.com/a/47664)

"service runs a script in a predictable environment (working directory is / and only 2 environment variables are set: LANG and TERM). It also adds the ability to do --full-restart. So to sum up:

service may run scripts from either /etc/init or /etc/init.d (upstart or System V)
service runs scripts in a predictable environment."

[Setting up Alpine Linux with Rootless Docker](https://virtualzone.de/posts/alpine-docker-rootless/). How will this work on WSL when the user has a bunch of privileges, like deleting all the users files, gifted by WSL?

[Docker Rootless mode](https://docs.docker.com/engine/security/rootless/) and [WSL2 configuration for developing using rootless docker](https://gist.github.com/espresso3389/a4aeeb1ce9d12c2b0d8b7409eed62e8c)

A good description of how to run anything [How to run htop in Docker terminal?](https://labex.io/tutorials/docker-how-to-run-htop-in-docker-terminal-415868)

[lazydocker](https://github.com/jesseduffield/lazydocker) for a docker management TUI.

all of this needs checking

[How to Install and Configure Docker on Alpine Linux](https://thelinuxcode.com/install-docker-alpine-linux/)

```bash
rc-update add docker boot
service docker start
docker run hello-world
```

[How to Create and Manage a Service in an Alpine Linux Container](https://medium.com/@mfranzon/how-to-create-and-manage-a-service-in-an-alpine-linux-container-93a97d5dad80)

details not important here (like monitor_directory.sh)

```Dockerfile
FROM alpine:latest
RUN apk update && \
    apk add openrc inotify-tools && \
    mkdir -p /run/openrc && \
    touch /run/openrc/softlevel
COPY monitor_directory.sh /usr/local/bin/monitor_directory.sh
COPY monitor_directory_service /etc/init.d/monitor_directory
RUN chmod +x /usr/local/bin/monitor_directory.sh && \
    chmod +x /etc/init.d/monitor_directory
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

`/etc/init.d/monitor_directory`

```sh
#!/sbin/openrc-run
name="Monitor Directory"
description="Monitor a directory"
command="/usr/local/bin/monitor_directory.sh"
command_background=true # needed for rc-service to stop, start, etc
pidfile="/run/monitor_directory.pid" # needed for rc-service to stop, start, etc
```

```sh
#!/bin/sh
openrc default
rc-update add monitor_directory default
rc-service monitor_directory start
exec "$@"
```

## Putty

I suggest that you [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to test out the connection on the Windows side.

On Windows run the "Device Manager" and expand the Ports (COM & LPT) section. Note the COM port number for the Pico; on my system it's labelled "USB Serial Device (COM7)".

Open PuTTY, select the Serial connection type and enter the COM7 (see above) in the Serial line box. Set the Speed to 115200 and click on the Open button. A window should open that repetitively prints "Hello, World!".

## Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
