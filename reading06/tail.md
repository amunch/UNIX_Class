TLDR - tail
==========

Overview
--------

[tail] is just like heaed, except it prints the last part of a file or stdout if piped into it.  By default, it will print the last 10 lines of a file.

Examples
--------

- **Print** the last 10 lines of a file:

        $ tail tail.md

- **Print** the least 5 lines of the stdout of a cat of the /etc/passwd file:

		$ cat /etc/passwd | tail -n 5 /etc/passwd

- **Follow** the output of a file as it grows, and *print* these to stdout:

		$ tail -f /var/log/wtmp

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/tail.1.html)

[tail]: http://man7.org/linux/man-pages/man1/tail.1.html

