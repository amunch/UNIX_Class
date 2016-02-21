TLDR - uniq
==========

Overview
--------

[uniq] analyzes a file and can either output what lines are repeated, or omit any lines that are repeated.  Also, you can print each line with the number of times it occurs.

Examples
--------

- **Analyze** a file, and *print* all of the repeated lines:

        $ uniq -d file.c

- **Analyze** a file, and *print* how many times each line occurs in the file: 

		$ uniq -c file.c

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/uniq.1.html)

[uniq]: http://man7.org/linux/man-pages/man1/uniq.1.html

