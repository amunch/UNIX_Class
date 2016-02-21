TLDR - comm
==========

Overview
--------

[comm] is a command that allows one to compare two files by line.  The output of this command includes the lines unique to file 1 in the first column, the lines unique to file 2 in the second column, and the common lines in the third column.

Examples
--------

- **Compare** two files, line by line:

        $ comm file1.c file2.c

- **Compare** two files, line by line, but only show the common lines between the two:

		$ comm -12 file1.c file2.c

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/comm.1.html)

[comm]: http://man7.org/linux/man-pages/man1/comm.1.html

