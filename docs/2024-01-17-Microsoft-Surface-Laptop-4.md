---
date: "2024-01-17"
title: "Microsoft Surface Laptop 4"
---
<!-- markdownlint-disable MD025 -->
# Microsoft Surface Laptop 4
<!-- markdownlint-enable MD025 -->

### PowerShell History

```PowerShell
hx (Get-PSReadlineOption).HistorySavePath # hx is Helix Editor
```

## Building a Boot Disk

[Create a recovery drive (WinRE)](https://support.microsoft.com/en-us/windows/create-a-recovery-drive-abb4691b-5324-6d4a-8766-73fab304c246) using the control panel from a existing version of windows, [create Windows 11 installation media](https://www.microsoft.com/en-gb/software-download/windows11) or build [Windows PE (WinPE)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-intro?view=windows-11) as described below.

[Install the Windows ADK offline](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-offline-install) and add [the WinPE add-on](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-install):

[A comprehensive description of a WinPE installation USB](https://superuser.com/a/1632315)
[WinPE - Create a Custom Windows Install USB](https://www.elevenforum.com/t/winpe-create-a-custom-windows-install-usb.4804/)
[Install Windows 11 using WinPE usb on any partition by typing setup at command prompt.](https://www.elevenforum.com/t/install-windows-11-using-winpe-usb-on-any-partition-by-typing-setup-at-command-prompt.9160/)

```PowerShell
cd "$env:HOMEPATH\Downloads\Windows Kits\10\ADK"
.\adksetup.exe /quiet /installpath c:\ADK /features OptionId.DeploymentTools
.\adkwinpesetup.exe /quiet /installpath c:\ADK /features OptionId.WindowsPreinstallationEnvironment
```

To find out what features can be installed, use the list option (/help for more options):

```PowerShell
.\adksetup /list # OptionId.DeploymentTools
.\adkwinpesetup.exe /list # OptionId.WindowsPreinstallationEnvironment
```

```PowerShell
diskpart
List disk
select disk X # X is the USB drive
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

run `Deployment and Imaging Tools Environment` app as administrator

```cmd
Makewinpemedia /ufd C:\WinPE_amd64 P:
xcopy C:\Images\install.wim I:\install.wim # path to install image # Image
```

### WinPE Startup

[Windows PE startup](https://oofhours.com/2020/12/03/windows-pe-startup-revisited/)

see `X:\System32\wpeinit.log` for details.

So let’s review the default process:

* `winlogon.exe` runs `winpeshl.exe`
* `winpeshl.exe` runs `“cmd.exe /k startnet.cmd”`
* `startnet.cmd` runs `wpeinit.exe`

You’re left sitting at a command prompt. Windows PE will reboot on `exit` (if exit code is 0). You can change every part of this:

* Changing `HKLM\System\Setup\CmdLine` isn't recommended.
* `winpeshl.ini` can run something other than `“cmd.exe /k startnet.cmd”`
* `“startnet.cmd”`` could run something else.
* Add an `unattend.xml` for `wpeinit.exe`.

Wait until networking and optional components are initialized.

Now look at how MDT does it:

* `winlogon.exe` runs `winpeshl.exe`
* `winpeshl.ini` includes `“bddrun.exe /bootstrap”`
* `bddrun.exe` runs `wpeinit.exe`
* `unattend.xml` runs the `“wscript.exe X:\Deploy\Scripts\LiteTouch.wsf”`
* When `wscript.exe` exits the machine reboots

All of the above avoids displaying a command prompt (it's a series of Windows apps and not console apps) so no console access. To display something to the user HTA or popups can be used.

## Adding Drivers to Boot Media

See [the official documentation](https://learn.microsoft.com/en-us/surface/enable-surface-keyboard-for-windows-pe-deployment#add-keyboard-drivers-to-the-selection-profile) or [this write up](https://www.risual.com/2022/03/adding-surface-drivers-to-windows-image/) for more information. The drivers and firmware for "Surface Laptop 4 with AMD Processor" are [here](https://www.microsoft.com/en-us/download/details.aspx?id=102923). To extract these run:

```PowerShell
Msiexec.exe /a SurfaceLaptop4_AMD_Win11_22000_23.120.1653.0.msi /qb targetdir=c:\surface_laptop
```

Then add these files to the `boot.wim` (or another image file):

```PowerShell
mkdir "c:\winboot"
mkdir "c:\winboot\mount"
$BootWimSource = "D:\sources\boot.wim" 
$MountPath = "c:\winboot\mount" 
$BootWim = "c:\winboot\boot.wim"
$drivers = "C:\surface_laptop"
copy $BootWimSource $BootWim
Mount-WindowsImage -Path $MountPath -ImagePath $BootWim -Index 1 # service
Add-WindowsDriver -Path $MountPath -Driver $drivers -Recurse
Dismount-WindowsImage -Path $MountPath –Save
copy $BootWim $BootWimSource
```

The set of drivers for "Surface Laptop 4 with AMD processor" are [listed in a table](https://learn.microsoft.com/en-us/surface/enable-surface-keyboard-for-windows-pe-deployment#add-keyboard-drivers-to-the-selection-profile)

```output
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

```output
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
```

## WinPE Extra Tools

* [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)
* [NotePad++](https://notepad-plus-plus.org/downloads/)
* [Neovim](https://github.com/neovim/neovim/releases/)
* [Explorer++](https://explorerplusplus.com/)
* [Adding DaRT to ConfigMgr Boot Images – And starting it earlier than early](https://www.deploymentresearch.com/adding-dart-to-configmgr-boot-images-and-starting-it-earlier-than-early/)
* [How to run Microsoft Network Monitor in WinPE](https://www.deploymentresearch.com/how-to-run-microsoft-network-monitor-in-winpe/)

To [add PowerShell](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-adding-powershell-support-to-windows-pe?view=windows-11),
start the "Deployment and Imaging Tools Environment" as an administrator and run these commands:

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

## Image Management

```shell
# Capture Multiple Partitions
diskpart
list volume
select partition=x # x is number of partition to rename
assign letter=s
exit

DISM /image:C:\ /optimize-image /boot
Dism /Capture-Image /ImageFile:E:\windows.wim /CaptureDir:C:\ /Name:"Windows" /CheckIntegrity # /Compress:{fast|max|none} default max
Dism /Capture-Image /ImageFile:C:\my-system-partition.wim /CaptureDir:S:\ /Name:"My system partition"

# Apply Image
Set high-performance power scheme to speed deployment
call powercfg /s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

dism /Apply-Image /ImageFile:E:\Images\ThinImage.wim /Index:1 /ApplyDir:W:\

# Copy boot files to the System partition
W:\Windows\System32\bcdboot W:\Windows /s S:

# Copy the Windows RE image to the Windows RE Tools partition
md R:\Recovery\WindowsRE
xcopy /h W:\Windows\System32\Recovery\Winre.wim R:\Recovery\WindowsRE\

# Register the location of the recovery tools
W:\Windows\System32\Reagentc /Setreimage /Path R:\Recovery\WindowsRE /Target W:\Windows

# Verify the configuration status of the images
W:\Windows\System32\Reagentc /Info /Target W:\Windows

# FFU
DISM.exe /capture-ffu /imagefile=e:\windows.ffu /capturedrive=\\.\PhysicalDrive0 /name:disk0 /description:"Windows FFU"
```

* [Capture and apply Windows, system, and recovery partitions](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-system-and-recovery-partitions?view=windows-11)
* [Image Deployment Sample scripts](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?preserve-view=true&view=windows-10#-createpartitions-uefitxt)
* [diskpart](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)
* [Capture and apply Windows Full Flash Update (FFU) images](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/deploy-windows-using-full-flash-update--ffu?view=windows-11)
* [How to convert install.esd to install.wim](https://www.youtube.com/watch?v=u44hggPLu7w)

```PowerShell
# Admin
dism /get-wiminfo /wimfile:"e:\sources\install.esd" # number 6 is Professional
mkdir c:\temp
# compress max not required, expecially if exporting to install.esd later
dism /export-image /sourceimagefile:"e:\sources\install.esd" /SourceIndex:6 /DestinationImageFile:c:\temp\install.wim /compress:max /checkintegrity
Mount-WindowsImage -path c:\mnt -imagepath C:\temp\install.wim -index 1
Add-WindowsDriver -Path c:\mnt -Driver C:\surface\ -Recurse
Dismount-WindowsImage -Path c:\mnt -save
# may not need to do this, could leave it as install.wim
dism /export-image /sourceimagefile:c:\temp\install.wim /sourceIndex:1 /destinationimagefile:c:\temp\install.esd /compress:recovery
rename-item e:\install.esd e:\install.esd.old
copy c:\temp\install.esd e:\sources\install.esd
```

[Split a Windows image file (.wim)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/split-a-windows-image--wim--file-to-span-across-multiple-dvds?view=windows-11)

```PowerShell
# similarly, with `swm` filesh
dism /export-image /sourceimagefile:"c:\esd\install.swm" /SourceIndex:1 /DestinationImageFile:c:\temp\install_home.wim /compress:max /checkintegrity
Mount-WindowsImage -path c:\mnt -imagepath C:\temp\install_home.wim -index 1
Add-WindowsDriver -Path c:\mnt -Driver C:\surface_laptop\ -Recurse
Dismount-WinowsImage -Path c:\mnt -save
Dism /Split-Image /ImageFile:C:\temp\install_home.wim /SWMFile:C:\temp\install_home.swm /FileSize:4000
copy C:\temp\install_home*.swm d:\sources
```

[DISM Image Management Command-Line Options](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14?view=windows-11#export-image)

"Use the recovery option to export push-button reset images. The resulting files are much smaller in size, which in turn, greatly reduce the amount of disk space needed for saving the push-button reset image on a recovery drive. The destination file must be specified with an .esd extension."

This appears to be used with both [Windows Recovery Environment (Windows RE)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference?view=windows-11) and [Push-button reset](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/push-button-reset-overview?view=windows-11)

[What is the most efficient, native way to image a Windows partition?](https://superuser.com/a/1581804)

"ESDs (Electronic Software Distribution) can only capture a System partition and must use /Compress:Recovery (algorithm is ~33% more efficient than /Compress:Max)
Windows ≥ 10: Can only be used for PBR [Push-Button Reset] exported image"

[WIM - This paper defines the internal format of a Windows Imaging (WIM) file format](https://www.microsoft.com/en-us/download/details.aspx?id=13096)

## Insalling Windows 11

"For Windows 11: If you're launching Windows Setup from WinPE, make sure your WinPE image includes the [WinPE-WMI and WinPE-SecureStartup optional components](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-add-packages--optional-components-reference?view=windows-11#winpe-optional-components)"

[Windows Setup Supported Platforms and Cross-Platform Deployments](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-supported-platforms-and-cross-platform-deployments?view=windows-11):

* Run a 32-bit version of Windows Setup, and use the /InstallFrom command-line option to select a 64-bit Windows image: `D:\setup.exe /InstallFrom:"N:\Windows_64-bit\sources\install.wim"`
* Run a 32-bit version of Windows Setup, and use the Microsoft-Windows-Setup\ImageInstall\OSImage\InstallFrom unattend setting to select a 64-bit Windows image: `D:\setup.exe /unattend:"D:\unattend_install_64-bit.xml"`
* Use image-capturing tools to apply a 64-bit version of Windows to the PC: `Dism /Apply-Image /ImageFile:"Fabrikam_64-bit_image.wim" /Index:1 /ApplyDir:D:\`

[Windows Setup Edition Configuration and Product ID Files (EI.cfg and PID.txt)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-edition-configuration-and-product-id-files--eicfg-and-pidtxt?view=windows-11)

ei.cfg

```text
[EditionID]
Professional
[Channel]
Retail
[VL]
0
```

PID.txt

```text
[PID]
Value=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
```

## Application Setup

[Chocolatey vs. Scoop vs. Winget: Package Managers for Windows](https://www.bowmanjd.com/chocolatey-scoop-winget/)

[Chocolatey and Winget Comparison](https://github.com/ScoopInstaller/Scoop/wiki/Chocolatey-and-Winget-Comparison)

[PowerShell Gallery](https://www.powershellgallery.com/)

[PowerShell Crescendo - working with existing command line tools](https://github.com/PowerShell/Crescendo)

[My Crescendo journey](https://devblogs.microsoft.com/powershell-community/my-crescendo-journey/) and [Crescendo - PowerShell Community](https://devblogs.microsoft.com/powershell-community/tag/crescendo/)

```PowerShell
https://aka.ms/PSWindows # upgrade powershell
# admin user
Set-ExecutionPolicy AllSigned
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
winget upgrade --all
winget install --id Git.Git -e --source winget
winget install chezmoi
chezmoi init https://github.com/$GITHUB_USERNAME/dotfiles.git
chezmoi diff # check possible changes
# chezmoi apply # optinally apply
# as admin for winget import
winget import -i $env:USERPROFILE\.config\windows_config\winget.json --accept-package-agreements
# winget export -o $env:USERPROFILE\.config\windows_config\winget.json
# as admin for choco
iwr -useb chocolatey.org/install.ps1 | iex
choco install "$env:USERPROFILE\.config\windows_config\choco_packages.config"
# choco export "$env:USERPROFILE\.config\windows_config\choco_packages.config"
# as normal user for scoop
iwr -useb get.scoop.sh | iex
scoop import > $env:USERPROFILE\.config\windows_config\scoopfile.json
# scoop export > $env:USERPROFILE\.config\windows_config\scoopfile.json
# Set Git Credential Manager Core by running: 
git config --global credential.helper manager
# To add context menu entries, run
'C:\Users\jackc\scoop\apps\git\current\install-context.reg'
# To create file-associations for .git* and .sh files, run
'C:\Users\jackc\scoop\apps\git\current\install-file-associations.reg'
cd $env:HOMEPATH
mkdir git
cd git
git clone https://github.com/jchidley/mkdocs-material-test.git
# run windows update
iwr -useb https://christitus.com/win | iex
```

## Windows Intune / Autopilot

If you try to install the *Professional* version of windows and the previous owner of the laptop has added it to *Windows Intune* or *Autopilot* then you will need to install the *Home* edition first and then upgrade it to *Pro*.

### Chezmoi and dotfiles

* [Chezmoi](https://www.chezmoi.io/)
* [chezmoi - Dotfiles Manager across multiple machines | Tom Payne (the creator of it)](https://www.youtube.com/watch?v=JrCMCdvoMAw)
* [Solving the Dotfiles Problem (And Learning Bash)](https://www.youtube.com/watch?v=mSXOYhfDFYo) is very well explained
* [Chezmoi and Ansible](https://www.youtube.com/watch?v=-RkANM9FfTM)
* [Easily moving Linux installs](https://www.youtube.com/watch?v=x6063EuxfEA)
* [chezmoi: Organize your dotfiles across multiple computers | Let's Code](https://www.youtube.com/watch?v=L_Y3s0PS_Cg)
* [Using Chezmoi to Automate dotfiles / Config Files (+ my bashrc)](https://www.youtube.com/watch?v=id5UKYuX4-A&list=WL)
* [Dotfiles! Here's how I organize them](https://www.youtube.com/watch?v=5oXy6ktYs7I&t=449s)

## Fixing problems

[Fix Your Windows PC Problems](https://www.youtube.com/watch?v=v0pFyWXp540)

```shell
dism command using your windows image
dism /image:c:\ /cleanup-image /restorehealth /source:c:\windows

# Add this command you yours and change path to your path
/scratchdir:{path}

# This command uses the windows image on USB drive we created.
dism /image:c:\ /cleanup-image /restorehealth /source:{path to install.wim or install.esd}

sfc /scannow from windows recovery
sfc /scannow /offbootdir={drive}\ /offwindir={drive}\windows
```

* [How To Make Microsoft Edge Better](https://www.youtube.com/watch?v=VgBsrvSSPyc)
* [Windows 11 Fixer](https://github.com/99natmar99/Windows-11-Fixer)
* [The Ultimate Windows Utility](https://christitus.com/windows-tool/)
* [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)

## Links

Checkout surface backup

* [Download drivers and firmware for Surface](https://support.microsoft.com/en-us/surface/download-drivers-and-firmware-for-surface-09bb2e09-2a4b-cb69-0951-078a7739e120#bkmk_update-manually)
* [Where to look for your BitLocker recovery key](https://support.microsoft.com/en-us/windows/where-to-look-for-your-bitlocker-recovery-key-fd2b3501-a4b9-61e9-f5e6-2a545ad77b3e)
* [Surface Recovery Image Download](https://support.microsoft.com/en-gb/surface-recovery-image)
* [Creating and using a USB recovery drive for Surface](https://support.microsoft.com/en-us/surface/creating-and-using-a-usb-recovery-drive-for-surface-677852e2-ed34-45cb-40ef-398fc7d62c07)
* [Restore or reset Surface for Windows](https://support.microsoft.com/en-us/surface/restore-or-reset-surface-for-windows-e1fd649a-6396-a7de-2e87-7ba3b45e0fb1)
* [Linux running on the Microsoft Surface devices. Follow the instructions below to install the latest kernel.](https://github.com/linux-surface/linux-surface/wiki/Installation-and-Setup)

* [Install Windows the Arch Linux Way](https://christitus.com/install-windows-the-arch-linux-way/)
* [Reagentc Windows Recovery Partition](https://christitus.com/reagentc-windows-recovery-partition/)
* [Chris Titus Tech Utility](https://www.youtube.com/watch?v=XQAIYCT4f8Q) `iwr -useb https://christitus.com/win | iex`
* [Windows 11 Perfect Install](https://christitus.com/windows-11-perfect-install/)
