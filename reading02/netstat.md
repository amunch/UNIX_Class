TLDR - netstat
==========

Overview
--------

[netstat] prints the status of the network, which includes all of the network connections the host currently has.  In addition, it lists all routing table, interface stats, masquerade connections, and multicast memberships.

Examples
--------

- **List** the *connections* of the current host:

        $ netstat

- **List** the *connections*, but also display the file name of the process, rather than the PID.  Note, this may increase the time it takes for netstat to execute:

		$ netstat -b

- **List** the *connections*, along with detailed statistics for each protocol:

		$ netstat -s

Resources
---------

- [man7](http://man7.org/linux/man-pages/man8/netstat.8.html)

[netstat]: http://man7.org/linux/man-pages/man8/netstat.8.html

