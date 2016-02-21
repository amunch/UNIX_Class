TLDR - grep
==========

Overview
--------

[grep] will send to stdout all of the lines in stdin matching a specified pattern.

Examples
--------

- **Print** all of the lines having the pattern "bin" in it from the /etc/passwd file:

        $ cat /etc/passwd | grep "bin"

- **Print** all of the lines in /etc/passwd that contain ":", but whose immediate next character is not 4.

		$ cat /etc/passwd | grep ":[^4]"

- **Print** all of the lines containing double vowels in /etc/passwd:

		$ cat /etc/passwd | grep -E "[AEIOUaeiou]{2}" 

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/grep.1.html)

[grep]: http://man7.org/linux/man-pages/man1/grep.1.html

