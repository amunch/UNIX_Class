TLDR - ldd
==========

Overview
--------

[ldd] is used on dynamic executables.  It prints the shared libraries that are required to run the program, and these libraries will be used when the executable is run.

Examples
--------

- **List** the shared libraries that are required by the executable a.out:

        $ ldd a.out

- **List** the shared libaries that are required by a.out, but this time incude more details such as the versions.

		$ ldd -v a.out

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/ldd.1.html)

[ldd]: http://man7.org/linux/man-pages/man1/ldd.1.html

