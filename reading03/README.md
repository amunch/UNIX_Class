Reading 03
==========

*1.* To view all the text for a command, we first need to know where that command is located.  A quick whereis ls tells us that ls is located in /bin/ls, and I will use the strings command to view the text:

	$ string /bin/ls

*2.* To determine which shared libraries ls requires, use the ldd command:

	$ ldd /bin/ls

*3.* To list all of the system calls during an invocation of ls, use the strace command:

	$ strace /bin/ls

*4.* To debug the hello-debug program, run the gdb command.  The compiling of the program should have include the -g flag.  Once the gdb program is entered, hit run and gdb will run the program and help to debug:

	$ gdb hello-debug
	(gdb) run

*5.* Valgrind is the best tool to check for memory leaks.  Valgrind will return a summary of memory usage and any possible leaks, as well as errors.  To use this command, simply type valgrind and then your executable:

	$ valgrind hello-dynamic

*6.* To find any bottlenecks in the program, first compile with the makefile and then run the program:
	
	$ hello-profile

This creates a file called gmon.out, which allows us to find these bottlenecks.  Next, we use the gprof command to analyze the running of hello-profile:

	$ gprof hello-profile


