TLDR - scp
==========

Overview
--------

[scp] uses ssh to securely transfer files between two computers.  It uses the same authentication as the usual ssh, including asking for passwords. 

Examples
--------

- **Securely Transfer** filename1 to another host username2 at their *specified host name*:

        $ scp username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/scp.1.html)

[scp]: http://man7.org/linux/man-pages/man1/scp.1.html

