Reading 01
==========

**1.** To create a file *private* that is only readable by you, first create the file by using the touch command: 
	
	$ touch private

Next, use the following chmod command to set the permissions to private and only readable by you:

	$ chmod 600 private

This will create the file private only readable by you.


**2.** To create a symobolic link in your home directory for the specified afs ppath, /afs/nd.edu/coursesp.16/cse/cse20189.01, use the ln command, with the -s option to create a symlink.  The form for this command is ln -s targetfile linkname:

	$ ln -s /afs/nd.edu/coursesp.16/cse/cse20189.01 cse202189

This will create the link cse202189 to the specified path, and all the user needs to do is type the following to go to that directory:

	$ cd cse202189


**3.**
