TLDR - strace
==========

Overview
--------

[strace] is used to determine all of the system calls and signals occuring when a program is run.  It is often used for debugging, and works by recording all of the system calls to the terminal when a program is executed.

Examples
--------

- **List** all of the *system calls* called when the a.out executable is run:

        $ strace a.out

- **List** all of the *system calls*, but this time count the time and the number of errors for each system call.  This is a very nice way to see all of the calls and time in a very organized manner.  Always use this.

		$ strace -c a.out

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/strace.1.html)

[strace]: http://man7.org/linux/man-pages/man1/strace.1.html

