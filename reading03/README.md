Reading 03
==========

*1.* To view all the text for a command, we first need to know where that command is located.  A quick whereis ls tells us that ls is located in /bin/ls, and I will use the strings command to view the text:

	$ string /bin/ls

*2.* To determine which shared libraries ls requires, use the ldd command:

	$ ldd /bin/ls

*3.* To list all of the system calls during an invocation of ls, use the strace command:

	$ strace /bin/ls

*4.* 
