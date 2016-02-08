TLDR - sudo
==========

Overview
--------

[sudo] is a utility that allows a user to run commands as the root user (superuser).  It is used when the current permissions of a user are not sufficient to run a certain command.

Examples
--------

- **List** the commands that are currently able to be run by the current user on the current host:

        $ sudo -l

- **Run** the ls command as the *superuser*:

		$ sudo ls

Resources
---------

- [man7](https://www.sudo.ws/man/sudo.man.html)

[sudo]: https://www.sudo.ws/man/sudo.man.html

