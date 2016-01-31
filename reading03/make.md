TLDR - make
==========

Overview
--------

[make] is a utility that runs commands specified in a *Makefile*.  It has built in the ability to determine if a certain program has changed and needs to be recompiled, and is very useful with large programs with large compile times.

Examples
--------

- **Make** the program by running the commands as listed in the created Makefile.  Usually, I use the all rule as my first line and make automatically runs this first line and anything else that needs to be run to run this line.

        $ make

- **Make** the target hello-dynamic, as specified in the *Makefile*.  This likely will run a compilation command and create an executable.

	$ make hello-dynamic

- **Run** the target clean, which customarily cleans the executables created by the Makefile.

	$ make clean

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/make.1.html)

[make]: http://man7.org/linux/man-pages/man1/make.1.html

