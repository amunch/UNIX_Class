Homework 08
===========

*timeout.py*

**1)** The parent ran the main Python process, and the child process is forked to attempt to run the inputted commands.  This script low-level system calls.  os.fork() creates a child process, and within this process os.execvp on the command is used to run that process in the terminal.  The parent waits for the child process to execute its action and if it is not successful it outputs the errors.

**2)** The timeout mechanism works by first instantiating an alarm in the parent process set for how many seconds the user desired, defaulting to 10 seconds.  In the parent process, if the child process does not finish before the alarm goes off, an OSError will be thrown, the process will be killed, and the parent will wait on the child again to get the error and the pid.  As described above, forking and waiting are used on a forked process.  Also, a file object is opened to read the yaml file.  

**3)** The test script first checks to make sure that the program is executable by using the test -x on the file timeout.py.  It then checks to make sure that the right version of pyhton is used by cat-ing the timeout.py file, taking only the first line, and then grepping to see if python2.7 is there.  To check that a good statement is outputted to stderr by redirecting stderr to stdout using 2>&1, and then I chose to grep for usage.  If this was not shown, I outputted the failure message.  For the next 2, I created a sequence using the seq command.  For every number in the sequence, I tested on the slpp command and tested for success and failure and various commands that should output success or failure(using the && after a successful command and the || after the failure.  I then checked for relevant debugging message in the same method as the stderr redirect, grepping for Forking.

**4)** I used the following the script to test the command:

	#!/bin/sh

	cmd="./timeout.py -t 2 sleep 2"

	for i in $(seq 300); do
        	echo $i
        	$cmd
	done


I personally got it where none of my commands worked succesfully, all of them tripped the timer.  Dr. Bui noted that some should and some should not run successfully, so it must depend on the machine I am using.  I suspect that it just depends on how long it takes the process to complete relative to the alarm tripping.  Therefore, it is not reasonable to expect consistent results; factors include the speed of the machine and the process being run.

*rorschach.py*

**1)** I used the os.walk function that recursively searches through the inputted directory.  This was checked every time by using a while loop that continuously looped through until the user manually quit.  I only looped though the files, as we are not concerned with directories, only what is within them.  If multiple directories were specified I looped through each of these directories to all of these walks and the subsequent actions.

**2)** I first opened the file as readonly using the following line of code:

	INFILE = file(RULES, 'r')

which returns a file object.  I then loaded this yaml file into a variable called RULES using the following command:

	RULES = yaml.load(INFILE)

This load function returns a dictionary, which action and pattern being the keys and the desired action and pattern as the value of these keys.  I then used re_match and fnmatch to see if the pattern was in the name of the file.  If there are multiple rules, then I looped through each of these, and called the pattern by using rule['pattern'] which returned the pattern match for each rule.

**3)**  I created a dictionary where the key is each of the files in the given directories and the value at the keys is the most recent modified time.  I built this array before i began looping through the actions, and then used an if statement to test if a given files was in this array.  If it was not, this was a new file and was added to the array, and the command was executed (assuming it matched the pattern).  Otherwise, if the time did not match the previous key for that element, I redid this time and ran the command as this indicates a modification.

**4)**  I executed each action by looping through every file and running the following actions if the time was modified.  I first forked the process, and then for the child process ran the action using execvp.  The parent process waited on the child, and I also caught any exceptions that showed up.  I did this for every file that was modified in that waiting period.

**5)** It is my understanding that busy waiting relates to this program in that every time it loops through the program it checks every single files modify time.  IT would be nice to have the shell notify us with the information of a file if it has been created or modified, and then run the commands based on that.

With cache invalidation, if files are deleted we still have the old information in the dictionary.  os.walk only looks for files that exist obviously so if a file is deleted it will still be in the dictionary but is no longer necessary.  This can be alleviated by deleting entries that are not in the walk from time to time but would take up a large amount of processor time for every loop through.
