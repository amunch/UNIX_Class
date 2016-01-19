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


**3.** To determine the size of a file, use the ls command with the -l option to give a long description of the specified file.  For a file named BigFile, the following command can be used:
	
	$ ls -l BigFile

The output of the command will be something like the following:

	-rw-r--r--  1 andymunch  staff  30 Jan 17 21:04 BigFile

The number before the specified month, in this case 30, is the size of the file in bytes.

**4.** As with determining the size of a file, determining the size of a directory is similar, however, we use the du command, with the -h option ot make it more readable.

	$ du -h MyFolder

This will return something like the following:
	
	8.0K	MyFolder

This is the size of the directory, given in bytes.

**5.** ps ux brings up a list of processes, with the second column being the PID of that process. To kill that process, type kill followed by the PID.  In the case of ssh process given, with a PID of 25263, the follwing code will terminate the ssh student00 process.

	$ kill 25263

**6.** To kill all processes of a certain name, use the command killall followed by the name. For the urxvt processes, the following will kill all of that name:

	$ killall urvxt

**7.** To determine how long a program will take to execute, use the time command.  For more detailed information, use /usr/bin/time as the command.  The following will tell you how long a program named simulation will take to run.

	$ usr/bin/time simulation

**8.** To set your shell's editor to your desired editor, edit the .cshrc file with a text editor such as nano.  Add the following setenv lines to the file to set the default editor:

	setenv VISUAL vim
	setenv EDITOR vim

Where I have set my default editor to vim.	

	
