TLDR - nmap
==========

Overview
--------

[nmap] is a command which lists all of the open ports for a domain.  The nmap command returns a list which includes the name of the port, its status, and the service associated with it.  For example, nmap google.com returns services http amd https as open ports.

Examples
--------

- **List** ports available on google.com with their *status and service type*:

        $ nmap google.com

- **List** available ports, along with the -A option to tell you the version and OS of the mapped domain:

		$ nmap -A reddit.com

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/nmap.1.html)

[nmap]: http://man7.org/linux/man-pages/man1/nmap.1.html

