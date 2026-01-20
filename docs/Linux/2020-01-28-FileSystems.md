---
date: "2020-01-28"
title: "File systems"
tags:
  - linux
  - filesystem
  - ntfs
  - overlayfs
  - raspberry-pi
llm_assisted: true
---

!!! info "Reference"
    Notes on filesystems, NTFS access from Linux, and OverlayFS.
<!-- markdownlint-disable MD025 -->
# File systems
<!-- markdownlint-enable MD025 -->

## Introduction

## Working with Windows

Turn off faststart by:

```bat
powercfg /h off
```

Use [NTFS-3G](https://github.com/tuxera/ntfs-3g) to share data with Windows and Linux.  [Here is Arch Linux' information](https://wiki.archlinux.org/index.php/NTFS-3G).

```bash
pacman -S ntfs-3g
mkfs.ntfs # no need to be explicit in Arch Linux
mount /dev/sda2 /mnt # Arch linux support
```

In `/etc/fstab`:

```bash
# <file system>		<dir>		<type>	<options>	<dump>	<pass>
/dev/NTFS-part		/mnt/windows	ntfs-3g	defaults	0	0
```

### Raspberry Pi Overlay FS

* [Overlay FS in Raspi-config](https://pigeoncomputers.com/documentation/tips-and-tricks/overlay-file-system/) under Advanced Options, Overlay FS
* [Raspberry Pi Overlay Root Filesystem](https://yagrebu.net/unix/rpi-overlay.md) and [OverlayFS based reliable filesystem](https://github.com/ghollingworth/overlayfs) who is a [Raspberry Pi Engineer](https://forums.raspberrypi.com/viewtopic.php?f=63&t=253104&p=1549229#p1549229) apparently `sudo raspi-config nonint enable_overlayfs` or `sudo raspi-config nonint disable_overlayfs` does the trick or `enable_overlayfs()` `disable_overlayfs()` [according to](https://raspberrypi.stackexchange.com/questions/124628/raspbian-enable-disable-overlayfs-from-terminal)
[Docker and Overlay FS](https://stackoverflow.com/questions/70295287/run-docker-on-raspberry-pi4-with-overlay-fs)

## Links

* [Creating and using squashed file systems](https://www.tldp.org/HOWTO/SquashFS-HOWTO/creatingandusing.html)
* [Overlay filesystem](https://wiki.archlinux.org/index.php/Overlay_filesystem)
* [Overlay Filesystes](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt)
* [Full system backup with SquashFS](https://wiki.archlinux.org/index.php/Full_system_backup_with_SquashFS)
* [MBR file system identifiers](https://www.win.tue.nl/~aeb/partitions/partition_types-1.html)
* [Example OverlayFS Usage](https://askubuntu.com/questions/699565/example-overlayfs-usage)
* [OverlayFS](https://blog.programster.org/overlayfs)
* [How do I use OverlayFS](https://askubuntu.com/questions/109413/how-do-i-use-overlayfs/109441#109441)
* [Playing with overlayfs](http://jasonwryan.com/blog/2015/01/19/overlayfs/)
* [a practical look into overlayfs](https://ops.tips/notes/practical-look-into-overlayfs/)

<!-- markdownlint-disable MD034 -->
* https://askubuntu.com/questions/699565/example-overlayfs-usage
https://www.thegeekstuff.com/2017/05/sfdisk-examples/
https://wiki.archlinux.org/index.php/Fdisk
https://wiki.archlinux.org/index.php/GPT_fdisk#Convert_between_MBR_and_GPT
<!-- markdownlint-enable MD034 -->
