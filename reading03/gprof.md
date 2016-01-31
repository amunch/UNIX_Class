TLDR - gprof
==========

Overview
--------

[gprof] is a utility used to find parts of a program that take a large amount of time.  It is useful to determine bottlenecks.  When compiling the program, include the -pg flag and upon executing it will create the require gmon.out file.

Examples
--------

- **Create** the required gmon.out file for a program called hello.c.  Compile the program with the -pg flag and run the program.

        $ gcc -pg hello.c
	$ a.out

- **List times** taken for each *routine* in the program using gprof. A gmon.out file must have been created or this will throw an error.

	$ gprof a.out

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/gprof.1.html)

[gprof]: http://man7.org/linux/man-pages/man1/gprof.1.html

