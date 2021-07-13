# LINUX PACKAGE MANAGERS

Track all components of the software you install, making updates, reinstalls, troubleshooting much easier

Linux default method of installing applications: from a distribution software repository ~ app store

Arch and Gentoo distros that use neither dnf nor apt

## dnf
cli package management tool for installing software in 
- RHEL
- CentOS
- Fedora
- Mageia
- OpenMandriva...


## apt

For 
- Debian and Debian-based distros such as MX Linux
- Deepin
- Ubuntu—and distros based on Ubuntu such as Linux Mint and Pop!_OS—have 

### apt-related tools for installing software:
* [Synaptic](https://www.nongnu.org/synaptic/) 
graphical (GTK+) package management program for apt. It provides the same features as the apt-get command line utility with a GUI front-end based on Gtk+.

* [Aptitude](https://wiki.debian.org/Aptitude) 
an Ncurses-based full-screen command-line front end for apt.
There are apt-get, apt-cache, and other predecessors of apt.
Aptitude is an Ncurses and command-line based front-end to numerous Apt libraries, which are also used by Apt, the default Debian package manager. Aptitude is text based and run from a terminal.

Ncurses is a programming library providing an API, allowing the programmer to write text-based user interfaces, 

* [Dpkg](https://wiki.debian.org/Teams/Dpkg) 
a suite of programs used for low-level source and binary package management.
is the "behind the scenes" package manager apt uses to do the heavy lifting.

* [Flatpak](https://flatpak.org/)
Flatpak can be used with a total of 28 distros

* [Snap](https://snapcraft.io/)
The app store for Linux

snap is both the command line interface and the application package format
snapd is the background service that manages and maintains your snaps
snapcraft is the command and the framework used to build your own snaps
Snap Store provides a place to upload your snaps, and for users to browse and install

### apt commands

* Finding software with apt
>apt search cockpit
  Web Console for Linux servers

* Installing software with apt
>sudo apt install cockpit

* view package metadata
>apt show cockpit
Package: cockpit
Version: 238-1
Section: universe/admin
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Utopia Maintenance Team <pkg-utopia-maintainers@lists.alioth.debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 88.1 kB
Depends: cockpit-bridge (>= 238-1), cockpit-ws (>= 238-1), cockpit-system (>= 238-1)
Recommends: cockpit-storaged (>= 238-1), cockpit-networkmanager (>= 238-1), cockpit-packagekit (>= 238-1)
Suggests: cockpit-doc (>= 238-1), cockpit-pcp (>= 238-1), cockpit-machines (>= 238-1), xdg-utils
Homepage: https://cockpit-project.org/
Download-Size: 21.3 kB
APT-Sources: http://ca.archive.ubuntu.com/ubuntu hirsute/universe amd64 Packages
Description: Web Console for Linux servers
The Cockpit Web Console enables users to administer GNU/Linux servers using a web browser.

* What package provides a file you know that must be in a package?
>apt search qmake-qt5

Explore inside packages
>apt-file search qmake-qt5
qt5-qmake-bin: /usr/share/man/man1/qmake-qt5.1.gz

* What files are included in a package?
>apt-file list cockpit
cockpit: /usr/share/doc/cockpit/TODO.Debian
cockpit: /usr/share/doc/cockpit/changelog.Debian.gz
cockpit: /usr/share/doc/cockpit/copyright
cockpit: /usr/share/man/man1/cockpit.1.gz
cockpit: /usr/share/metainfo/cockpit.appdata.xml
cockpit: /usr/share/pixmaps/cockpit.png

* Removing an application
>sudo apt purge apt-file

Removing a package doesn't automatically remove all the dependencies that apt installs along the way. However, it's easy to carry out that little bit of tidying:
>sudo apt autoremove