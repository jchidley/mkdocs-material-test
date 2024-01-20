---
date: "2024-01-17"
title: "Microsoft Surface Laptop 4"
---
<!-- markdownlint-disable MD025 -->
# Template
<!-- markdownlint-enable MD025 -->

## Introduction

A sentence

## Links

Checkout surface backup

[Download drivers and firmware for Surface](https://support.microsoft.com/en-us/surface/download-drivers-and-firmware-for-surface-09bb2e09-2a4b-cb69-0951-078a7739e120#bkmk_update-manually)

[Where to look for your BitLocker recovery key](https://support.microsoft.com/en-us/windows/where-to-look-for-your-bitlocker-recovery-key-fd2b3501-a4b9-61e9-f5e6-2a545ad77b3e)

[Surface Recovery Image Download](https://support.microsoft.com/en-gb/surface-recovery-image)

[Creating and using a USB recovery drive for Surface](https://support.microsoft.com/en-us/surface/creating-and-using-a-usb-recovery-drive-for-surface-677852e2-ed34-45cb-40ef-398fc7d62c07)

[Restore or reset Surface for Windows](https://support.microsoft.com/en-us/surface/restore-or-reset-surface-for-windows-e1fd649a-6396-a7de-2e87-7ba3b45e0fb1)

[Linux running on the Microsoft Surface devices. Follow the instructions below to install the latest kernel.](https://github.com/linux-surface/linux-surface/wiki/Installation-and-Setup)

Device information:
Device name: LAPTOP...
Serial number: 0337...
Surface model: Surface Laptop 4 Model 1952:1953
SAM: 12.104.139.0
UEFI: 3.350.140.0
App version: 61.23120.85.0
BIOS Version/Date: Microsoft Corporation 3.350.140 05/02/2023
Touch driver: 5.0.132.139
WiFi driver: 22.230.0.8
Edition: Windows 11 Pro
OS build: 22631.3007
Processor: AMD Ryzen 7 Microsoft Surface (R) Edition
Installed RAM: 8 GB
Storage size: 56 GB free of 236 GB
GPU: AMD Radeon(TM) Graphics
Screen resolution: 2496 x 1664

## Installation

### Windows

[Install the Windows ADK offline](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-offline-install)

I put the files in my Downloads folder

```PowerShell
cd "$env:HOMEPATH\Downloads\Windows Kits\10\ADK"
.\adksetup.exe /quiet /installpath c:\ADK /features OptionId.DeploymentTools
.\adkwinpesetup.exe /quiet /installpath c:\ADK /features OptionId.WindowsPreinstallationEnvironment
```

```PowerShell
.\adksetup /list # Get a list of installable items
   # OptionId.DeploymentTools
.\adkwinpesetup.exe /list # /help
   # OptionId.WindowsPreinstallationEnvironmen
```

### Windows PE

[WinPE: Adding Windows PowerShell support to Windows PE](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-adding-powershell-support-to-windows-pe?view=windows-11)
Start the Deployment and Imaging Tools Environment as an administrator

```PowerShell
List disk
select disk X #   (where X is your USB drive)
clean
convert MBR
create partition primary size=2048
active
format fs=FAT32 quick label="WinPE"
assign letter=P
create partition primary
format fs=NTFS quick label="Images"
assign letter=I  
Exit
```

run `Deployment and Imaging Tools Environment` app

```cmd
copype amd64 C:\WinPE_amd64
```

[Adding Surface drivers to Windows image](https://www.risual.com/2022/03/adding-surface-drivers-to-windows-image/)

```PowerShell
$MountPath = "C:\WinPE_amd64\mount" 
$WinPE = "C:\WinPE_amd64\media\sources\boot.wim"
$drivers = "C:\surface_laptop\SurfaceUpdate"
Mount-WindowsImage -Path $MountPath -ImagePath $WinPE -Index 1 # service
Add-WindowsDriver -Path $MountPath -Driver $drivers -Recurse
Dismount-WindowsImage -Path $MountPath –Save
```

The set of drivers for my "Surface Laptop 4 with AMD processor" can are listed in a table in [How to enable the Surface Laptop keyboard during MDT deployment](https://learn.microsoft.com/en-us/surface/enable-surface-keyboard-for-windows-pe-deployment#add-keyboard-drivers-to-the-selection-profile) link

```PowerShell
U0361415
AMDfendr
AMDGpio2
AMDI2c
AMDLpcFilterDriverAMDMicroPEP
AMDPsp
AMDSmf
AMDSpi
AMDUart
SurfaceEthernetAdapter
SMBUS
SurfaceBattery
SurfaceButton
SurfaceDigitizerHidSpiExtnPackage
SurfaceHIDFriendlyNames
SurfaceHidMini
SurfaceHotPlug
SurfaceOemPanel
SurfacePowerMeter
SurfacePowerTrackerCore
SurfaceSerialHub
SurfaceSMFClient
SurfaceSmfDisplayClient
SurfaceSystemManagementFramework
SurfaceTconDriver
SurfaceThermalPolicy
Surfacetimealarmacpifilter
SurfaceUcmUcsiHidClient
```

run `Deployment and Imaging Tools Environment` app as administrator

```cmd
Makewinpemedia /ufd C:\WinPE_amd64 P:
xcopy C:\Images\install.wim I:\install.wim # path to install image # Image
```

```shell
$APK = "C:\\Program Files (x86)\Windows Kits\10"
# mount path as above
# nvim search/replace - select range, :, then
# /C:\\WinPE_amd64_PS\\mount/$MountPath/g
# /C:\\Program Files \(x86\)\\Windows Kits\\10/$APK/g
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-WMI.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-WMI_en-us.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-NetFX.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-NetFX_en-us.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-Scripting.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-Scripting_en-us.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-PowerShell.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-PowerShell_en-us.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-StorageWMI.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-StorageWMI_en-us.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-DismCmdlets.cab"
Dism /Add-Package /Image:"$MountPath" /PackagePath:"$APK\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\WinPE_OCs\en-us\WinPE-DismCmdlets_en-us.cab"
Dism /Unmount-Image /MountDir:"$MountPath" /Commit
```

After booting WinPE you can run powershell with this command `X:\Windows\system32\WindowsPowerShell\v1.0\powershell`

[Capture and apply Windows, system, and recovery partitions](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-system-and-recovery-partitions?view=windows-11)

This is a very easy way to lose your sanity: I have lost too many systems and too much data using tools like this (lots of different types systems, starting with DOS)
[Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
[Linux running on the Microsoft Surface devices](https://github.com/linux-surface/linux-surface)
[Install the Windows ADK offline](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-offline-install)
[Adding Surface drivers to Windows image](https://www.risual.com/2022/03/adding-surface-drivers-to-windows-image/)
[WinPE: Adding Windows PowerShell support to Windows PE](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-adding-powershell-support-to-windows-pe?view=windows-11)
[Image Deployment Sample scripts](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?preserve-view=true&view=windows-10#-createpartitions-uefitxt)
[diskpart](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)
[Capture and apply Windows Full Flash Update (FFU) images](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/deploy-windows-using-full-flash-update--ffu?view=windows-11)
