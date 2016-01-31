TLDR - strings
==========

Overview
--------

[strings] prints strings, specifically strings of characters that are 4 characters or longer, from a specified file.

Examples
--------

- **List** the strings in the binary of the *command ls*:

        $ strings /bin/ls

- **List** the strings in a file called hello.c. Use the -1 option such that the minimum length for a string to be printed is 1.

		$ strings -1 hello.c

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/strings.1.html)

[strings]: http://man7.org/linux/man-pages/man1/strings.1.html

