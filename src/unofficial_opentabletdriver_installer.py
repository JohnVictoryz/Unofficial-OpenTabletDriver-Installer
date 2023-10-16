# Unofficial OpenTabletDriver Installer

import distro as ds
import os
import requests as req
from platform import platform as os_platform
from rich import print
import time
from urllib.request import urlretrieve as get
import subprocess as sp
platform = os_platform()
if "Windows" in platform:    
    import zipfile

dotnet_win_installer_url = "https://opentabletdriver.net/Framework"
dotnet_win_installer_filename = "%temp%\dotnet.exe"
opentabletdriver_win_url = "https://opentabletdriver.net/Release/Download/OpenTabletDriver.win-x64.zip"
opentabletdriver_win_filename = "%temp%\OpenTabletDriver.zip"
startmenu_folder = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
bat_file_url = ""
bat_file_name = "%localappdata%\OpenTabletDriver\OpenTabletDriver.bat"
opentabletdriver_debian_url = "https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.6.3.0/OpenTabletDriver.deb"
opentabletdriver_debian_filename = "/tmp/OpenTabletDriver.deb"
dotnet_debian_filename = "/tmp/dotnet.deb"
dotnet_debian_12_url = "https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb"
dotnet_debian_11_url = "https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb"
dotnet_debian_10_url = "https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb"
dotnet_debian_9_url = "https://packages.microsoft.com/config/debian/9/multiarch/packages-microsoft-prod.deb"
dotnet_debian_8_url = "https://packages.microsoft.com/config/debian/8/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_filename = "/tmp/OpenTabletDriver.deb"
dotnet_ubuntu_1404_url = "https://packages.microsoft.com/config/ubuntu/14.04/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_1510_url = "https://packages.microsoft.com/config/ubuntu/15.10/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_1604_url = "https://packages.microsoft.com/config/ubuntu/16.04/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_1704_url = "https://packages.microsoft.com/config/ubuntu/17.04/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_1804_url = "https://packages.microsoft.com/config/ubuntu/18.04/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_1904_url = "https://packages.microsoft.com/config/ubuntu/19.04/multiarch/packages-microsoft-prod.deb"
dotnet_ubuntu_2004_url = "https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb"
dotnet_ubuntu_2104_url = "https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb"
dotnet_ubuntu_2204_url = "https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb"
dotnet_ubuntu_2304_url = "https://packages.microsoft.com/config/ubuntu/23.04/packages-microsoft-prod.deb"
if "Windows" in platform:
    username = os.getlogin()
if "Linux" in platform:
    distro = ds.name()

print(f'[bold blue]Hello And Welcome to the unofficial OpenTabletDriver Installer [/bold blue]')
print(f'[bold blue]It must be noted that if you are trying to install this using linux you should run the installer as superuser example: sudo ./installer [/bold blue]')
print(f'[bold red]It Must be noted that by contiuning the installation you agree with the LGPL 3.0 license that goes as follows [/bold red]')
time.sleep(3)
print(f'''[bold green]                    GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library. [/bold green]''')
agrement = input("Do you agree with the license and contine the installation (y/n)")
if agrement == "n":
    exit()

print(f'[bold green]Starting Installer OpenTabletDriver[/bold green]')


def win():
    print(f'[bold green]The Installer detected that you are running Microsoft Windows™ if this is not true type (n) without the brackets. if you think this is true just press enter to continue[/bold green]')
    sel = input()
    if sel == "n":
        exit()
    print(f'[bold blue]Installing dotnet[/bold blue]')
    get(dotnet_win_installer_url, dotnet_win_installer_filename)
    os.system("cd %temp% && dotnet.exe /quiet")
    print(f'[bold blue]Installing OpenTabletDriver[/bold blue]')
    get(opentabletdriver_win_url, opentabletdriver_win_filename)
    os.system("mkdir %localappdata%\OpenTabletDriver")
    with zipfile.ZipFile(opentabletdriver_win_filename, 'r') as zip_ref:
        zip_ref.extractall("%localappdata%\OpenTabletDriver")
    print(f'[bold blue]Making Shortcuts for OpenTabletDriver[/bold blue]')
    get(bat_file_url, bat_file_name)
    sp.call("""C:\\Windows\\System32\\powershell.exe $s=(New-Object -COM WScript.Shell).CreateShortcut('C:\\Users\{username}\\Desktop\\OpenTabletDriver.lnk');$s.TargetPath='%localappdata%\\OpenTabletDriver\\OpenTabletDriver.bat';$s.IconLocation='%localappdata%\\OpenTabletDriver\\OpenTabletDriver.UX.Wpf.exe';$s.Save()""", shell=True)
    sp.call("""C:\\Windows\\System32\\powershell.exe $s=(New-Object -COM WScript.Shell).CreateShortcut('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OpenTabletDriver.lnk');$s.TargetPath='%localappdata%\\OpenTabletDriver\\OpenTabletDriver.bat';$s.IconLocation='%localappdata%\\OpenTabletDriver\\OpenTabletDriver.UX.Wpf.exe';$s.Save()""", shell=True)
    print(f'[bold blue]Cleaning up[/bold blue]')
    os.remove(opentabletdriver_win_filename)
    os.remove("%temp%","dotnet.exe")
    os.remove("%temp%", "OpenTabletDriver.zip")
    print(f'[bold green]Install Finished. Do you want to open OpenTabletDriver now? [/bold green](y/n): ')
    if input() == "y":
        os.system("cd %localappdata/OpenTabletDriver && start OpenTabletDriver.UX.Wpf.exe")
    else:
        exit()
def linux():
    def wrong_distro():
        print(f'[bold green]Dont Worry we got you covered please select your distro option [Debian (d), Ubuntu (u), Arch Linux (a), gentoo(g)] if you didnt see your distro then its not supported by the installer and you should close this program now by either clicking the close button or press Ctrl+C. If you did though see it press the starting lowercase letter as shown in the brackets [/bold green]')
        res = input()
        if res == "d":
            debian()
        elif res == "u":
            ubuntu()
        elif res == "a":
            arch()
        elif res == "g":
            gentoo()
        else:
            print(f'[bold red]There is no such option as ({res})[/bold red]')
            exit()
    def debian():
        print(f'[bold red]The Installer detected you are running Debian on this machine if you are not running please press (n) without the brackets and the installer will let you select your distro if this is your machine please type debian release number to continue the installation[/bold red]')
        sel = input()
        if sel == "n":
            wrong_distro()
        elif sel == "12":
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_debian_12_url, dotnet_debian_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel == "11":
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_debian_11_url, dotnet_debian_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel == "10":
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_debian_10_url, dotnet_debian_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel == "9":
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_debian_9_url, dotnet_debian_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel == "8":
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_debian_8_url, dotnet_debian_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        else:
            print(f'[bold red]Error Selection either Invalid or Unavailable[/bold red]')
            exit()
    def ubuntu():
        print(f'[bold red]The Installer detected you are running Ubuntu on this machine if you are not running please press (n) without the brackets and the installer will let you select your distro if this is your machine please type ubuntu release number to continue the installation[/bold red]')
        sel = input()
        if sel == "n":
            wrong_distro()
        elif sel.startswith("14"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1404_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("15"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1510_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("16"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1604_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("17"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1704_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("18"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1804_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("19"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_1904_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("20"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_2004_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("21"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_2104_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("22"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_2204_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        elif sel.startswith("23"):
            print(f'[bold blue]Installing dotnet[/bold blue]')
            get(dotnet_ubuntu_2304_url, dotnet_ubuntu_filename)
            os.system("cd /tmp/ &&  dpkg -i dotnet.deb  &&  apt update &&  apt install -y apt-transprort-https &&  apt update &&  apt install -y dotnet-sdk-6.0")
            print(f'[bold blue]Downloading and installing OpenTabletDriver[/bold blue]')
            get(opentabletdriver_debian_url, opentabletdriver_debian_filename)
            os.system("cd /tmp/ &&  apt install -y ./OpenTabletDriver.deb")
            print(f'[bold blue]Reloading Services and Starting OpenTabletDriver Services[/bold blue]')
            os.system(" systemctl --user daemon-reload &&  systemctl --user enable opentabletdriver --now")
            print(f'[bold blue]Cleaning up[/bold blue]')
            os.system("rm -rf {dotnet_debian_filename} {opentabletdriver_debian_filename}")
            print(f'[bold green]Install Finished[/bold green]')
            exit()
        else:
            print(f'[bold red]Error Selection either Invalid or Unavailable[/bold red]')
            exit()
    
    def arch():
        print(f'[bold green]The Installer has detected that you are running arch linux or manjaro if you think this is a mistake please type (n) without the brackets if this is correct just press enter to continue.[/bold green]')
        sel = input()
        if sel == "n":
            wrong_distro()
        print(f'[bold blue]Installing Dependencies[/bold blue]')
        os.system("pacman -Syu && pacman -S git")
        print(f'[bold blue]Installing OpenTabletDriver[/bold blue]')
        os.system("git clone https://aur.archlinux.org/opentabletdriver.git /tmp/opentabletdriver && cd /tmp/opentabletdriver && makepkg -si")
        print(f'[bold blue]Reloading Services[/bold blue]')
        os.system("systemctl --user daemon-reload && systemctl enable opentabletdriver --now")
        print(f'[bold blue]Cleaning Up[/bold blue]')
        os.system("rm -rf /tmp/opentabletdriver")
        print(f'[bold green]Install Finished[/bold green]')
        exit()
    def gentoo():
        print(f'[bold blue]The installer has detected that you are running gentoo linux if you think this is a mistake please type (n) without the brackets to choose your distro if you think this is correct just press enter to continue[/bold blue]')
        sel = input()
        if sel == "n":
            wrong_distro()
        print(f'[bold blue]Installing Dependencies[/bold blue]')
        os.system("eselect repository enable guru")
        os.system("emerge --sync guru")
        print(f'[bold blue]Changing Configs[/bold blue]')
        with open("/etc/portage/package.accept_keywords", "a") as file:
            file.write("\nx11-drivers/OpenTabletDriver-bin ~amd64")
            file.close()
        print(f'[bold blue]Installing OpenTabletDriver-bin[/bold blue]')
        os.system("emerge OpenTabletDriver-bin")
        print(f'[bold green]Installer Finished[/bold green]')
        exit()
    if "Debian" in distro:
        debian()
    elif "Ubuntu" in distro:
        ubuntu()
    elif "Arch" in distro or "Manjaro" in distro:
        arch()
    elif "Gentoo" in distro:
        gentoo()
    else:
        print(f'[bold red]The Installer didnt recognize this distro if you think this is a mistake press (y) without the brackets')
        wr = input()
        if wr == "y":
            wrong_distro()

if "Windows" in platform:
    win()
elif "Linux" in platform:
    linux()
