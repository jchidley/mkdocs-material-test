---
date: "2023-09-24"
title: "Systems-on-Systems"
---
<!-- markdownlint-disable MD025 -->
# Systems-on-Systems
<!-- markdownlint-enable MD025 -->

## Here Stings, Environment, heredoc

Here documents (heredoc, here-documents), and to a lesser extent here string, are widely used for automation and in scripts. Alpine Linux, for example, uses them extensively.

After that, `expect`, is used to automate `stdin` with more control. [Pexpect ](https://pexpect.readthedocs.io/en/stable/) "s a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output" and there's a `rust` version [rexpect](https://github.com/rust-cli/rexpect).

The best reference is from the Linux Documentation Project's [Chapter 19. Here Documents](https://tldp.org/LDP/abs/html/here-docs.html), with lots of great examples.
[https://thelinuxcode.com/bash-heredoc-tutorial/](https://thelinuxcode.com/bash-heredoc-tutorial/)
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
App='eval "C:\Windows\notepad.exe" "'$winFn'"'
$App
EOF
```

using `sh` functions to generate scripts, from [alpine-chroot-install](https://github.com/alpinelinux/alpine-chroot-install). Note the use of `printf format [arguments]` as an alternative to `echo`. The Alpine guys are the masters of `sh` scripts, in my opinion.

```bash
gen_chroot_script() {
	cat <<-EOF
		#!/bin/sh
		set -e

		ENV_FILTER_REGEX='($(echo "$CHROOT_KEEP_VARS" | tr -s ' ' '|'))'
	EOF
	if [ -n "$QEMU_EMULATOR" ]; then
		printf 'export QEMU_EMULATOR="%s"' "$QEMU_EMULATOR"
	fi
	cat <<-'EOF'

		user='root'
		if [ $# -ge 2 ] && [ "$1" = '-u' ]; then
		    user="$2"; shift 2
		fi
		oldpwd="$(pwd)"
		[ "$(id -u)" -eq 0 ] || _sudo='sudo'

		tmpfile="$(mktemp)"
		chmod 644 "$tmpfile"
		export | sed -En "s/^([^=]+ ${ENV_FILTER_REGEX}=)('.*'|\".*\")$/\1\3/p" > "$tmpfile" || true

		cd "$(dirname "$0")"
		$_sudo mv "$tmpfile" env.sh
		$_sudo chroot . /usr/bin/env -i su -l "$user" \
		    sh -c ". /etc/profile; . /env.sh; cd '$oldpwd' 2>/dev/null; \"\$@\"" \
		    -- "${@:-sh}"
	EOF
	# NOTE: ash does not load login profile when run with QEMU user-mode
	# emulation (I have no clue why), that's why /etc/profile is sourced here.
}

gen_chroot_script > enter-chroot
chmod +x enter-chroot
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

# Virtual Machines

[Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server)

```sh
# PowerShell
Get-VM | Export-VM -Path D:\WindowsBackup\
```

# WSL

- [Import any Linux distribution to use with WSL](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro)
- [Awesome-WSL: Awesome list dedicated to Windows Subsystem for Linux](https://github.com/sirredbeard/Awesome-WSL#10-gui-apps)
- [How to add second WSL2 Ubuntu distro](https://superuser.com/questions/1515246/how-to-add-second-wsl2-ubuntu-distro-fresh-install)
- [ubuntu images](https://cloud-images.ubuntu.com/wsl/)
- [How to change default user in WSL Ubuntu bash on Windows 10](https://askubuntu.com/questions/816732/how-to-change-default-user-in-wsl-ubuntu-bash-on-windows-10)
- [WSL - Connect USB devices](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
- [usbipd-win](https://github.com/dorssel/usbipd-win)

### APT Extras Script (Ubuntu/WSL)

Here’s a ready-to-run Bash script that builds `baseline.txt`, `manual.txt`, `extras.txt`, echoes what each file is, and then prints a one-line summary for every package in `extras.txt`.

Save it as `make-extras.sh` and run with `bash make-extras.sh` (no sudo needed unless your logs require it).

```bash
#!/usr/bin/env bash
set -euo pipefail

# Dependencies check
need() { command -v "$1" >/dev/null 2>&1 || { echo "Missing required command: $1" >&2; exit 1; }; }
for cmd in zgrep awk sort head cut comm apt-mark apt-cache; do need "$cmd"; done

# Gather earliest install date from dpkg logs
earliest=$(zgrep -h " install " /var/log/dpkg.log* 2>/dev/null | awk '{print $1}' | sort | head -n1 || true)
if [[ -z "${earliest:-}" ]]; then
  echo "No install entries found in /var/log/dpkg.log* — nothing to do." >&2
  exit 1
fi

# Build baseline: packages installed on the earliest date
zgrep -h " install " /var/log/dpkg.log* \
  | awk -v d="$earliest" '$1==d{print $4}' \
  | cut -d: -f1 \
  | sort -u > baseline.txt

# Get all packages marked as manually installed
apt-mark showmanual | sort > manual.txt

# Subtract baseline from manual -> extras
# (Requires bash for process substitution)
comm -23 manual.txt <(sort baseline.txt) > extras.txt

# Echo what each file represents
echo
echo "baseline.txt – packages installed on the very first day ($earliest)"
echo "manual.txt   – everything marked manual"
echo "extras.txt   – your real extras (manual minus baseline)"
echo

# Quick counts
printf "Counts: baseline=%d, manual=%d, extras=%d\n" \
  "$(wc -l < baseline.txt)" \
  "$(wc -l < manual.txt)" \
  "$(wc -l < extras.txt)"
echo

# Summaries for extras (one line per package)
if [[ -s extras.txt ]]; then
  echo "Package summaries (extras):"
  xargs -a extras.txt apt-cache show \
    | awk -F': ' '/^Package/{pkg=$2} /^Description-en/{print pkg " - " $2}'
else
  echo "No extras found (extras.txt is empty)."
fi
```

Notes

- Output files are written to the current working directory (`baseline.txt`, `manual.txt`, `extras.txt`).
- Re-running the script overwrites these files with fresh results.
- Clean up with: `rm -f baseline.txt manual.txt extras.txt`.

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

## Find and Export WSL distro

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

## Custom Linux for WSL - Alpine

see [WSL_Alpine_build](https://github.com/jchidley/WSL_Alpine_build) for the my build script. This uses [alpine-chroot-install](https://github.com/alpinelinux/alpine-chroot-install) to install alpine in its own directory an an existing linux system. Run `destroy` to remove all the bindings.

[Build a Custom Linux Distribution for WSL](https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro)

[wsl.conf](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconf) which are system specific settings. see also [.wslconfig](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig) for settings for all wsl.

see [OpenRC](https://wiki.alpinelinux.org/wiki/OpenRC) for some information about that. [How to enable and start services on Alpine Linux](https://www.cyberciti.biz/faq/how-to-enable-and-start-services-on-alpine-linux/) is useful but the `rc` appears to be `openrc` now. `openrc shutdown` sort of shuts down alpine but `wsl -t` actually stops it.

```sh
rc-service {service-name} restart # OR
/etc/init.d/{service-name} restart
```

[What's the difference between "Service" and "/etc/init.d/"?](https://askubuntu.com/a/47664)

"service runs a script in a predictable environment (working directory is / and only 2 environment variables are set: LANG and TERM). It also adds the ability to do --full-restart. So to sum up:

service may run scripts from either /etc/init or /etc/init.d (upstart or System V)
service runs scripts in a predictable environment."

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

# Docker

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

# Putty

I suggest that you [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to test out the connection on the Windows side.

On Windows run the "Device Manager" and expand the Ports (COM & LPT) section. Note the COM port number for the Pico; on my system it's labelled "USB Serial Device (COM7)".

Open PuTTY, select the Serial connection type and enter the COM7 (see above) in the Serial line box. Set the Speed to 115200 and click on the Open button. A window should open that repetitively prints "Hello, World!".

# Links

<!-- markdownlint-disable MD034 -->
<!-- markdownlint-enable MD034 -->
