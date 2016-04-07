Homework 08
===========

**1)** The parent ran the main Python process, and the child process is forked to attempt to run the inputted commands.  This script low-level system calls.  os.fork() creates a child process, and within this process os.execvp on the command is used to run that process in the terminal.  The parent waits for the child process to execute its action and if it is not successful it outputs the errors.

**2)** The timeout mechanism works by first instantiating an alarm in the parent process set for how many seconds the user desired, defaulting to 10 seconds.  In the parent process, if the child process does not finish before the alarm goes off, an OSError will be thrown, the process will be killed, and the parent will wait on the child again to get the error and the pid.  As described above, forking and waiting are used on a forked process.  Also, a file object is opened to read the yaml file.  

**3)** The test script first checks to make sure that the program is executable by using the test -x on the file timeout.py.  It then checks to make sure that the right version of pyhton is used by cat-ing the timeout.py file, taking only the first line, and then grepping to see if python2.7 is there.  To check that a good statement is outputted to stderr by redirecting stderr to stdout using 2>&1, and then I chose to grep for usage.  If this was not shown, I outputted the failure message.  For the next 2, I created a sequence using the seq command.  For every number in the sequence, I tested on the slpp command and tested for success and failure and various commands that should output success or failure(using the && after a successful command and the || after the failure.  I then checked for relevant debugging message in the same method as the stderr redirect, grepping for Forking.

**4)** 
