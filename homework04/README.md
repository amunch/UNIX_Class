Homework 04
===========

**ACTIVITY 01: Bake**

*1)* (a) To set the variables and override if the user inputs a different variable along with the command.  The following notation was used, using parameter expansion:

	CFLAGS=${CFLAGS:--std=gnu99 -Wall}

This sets the default value of the CFLAGS variable to "--std=gnu99 -Wall". If the user says in the same line as the command CFLAGS=(), where () is the desired value of the variable, CFLAGS will now have that variable.  This works for the variables CC, CFLAGS, VERBOSE, and SUFFIXES.

(b) To iterate over all the files with the same suffix, I used a for loop as such, using the wildcard in order that the for loop will iterate over all files with the same suffix:

	for arg in *$SUFFIXES; do

For example if SUFFIXES is not redefined on the command line, this will iterate through all files that end with .c.  

(c) VERBOSE was handled by declaring a variable of the same name with the value 0, using the parameter expansion notation so that it can be redefined by declaring it during the command.  Then, within the for loop that iterates over all of the files with the same suffix, I used an if statement where if the VERBOSE variable is set to 1(true), it will echo the command used to compile.  If the VERBOSE variable was not declared as 1, this if statement will not evaluate.

(d) I used the fact that if the compilation did not succeed, then a file with the same name, without the suffix, would not be created.  I then used an if statement to test if a file with the same name, without the suffix, was created after the compilation.  I used the following:

	if [ ! -e $name ]; then

With -e telling if the file exists, for the test command.  Thus, this if statment will run if a file of the same name does not exist.  Within the if statement, I echoed that the compilation failed and exited with the nonzero exit status 1.

*2)* The biggest advantage I see with make over a shell script is that make has built in the ability to only compile those files that have been changed.  This can be a drawback, as I have had several times where I had to make clean as make did not recognize a certain change, but except for this incredibly infrequent times this is a huge benefit.  Shell scripts are more natural, and the syntax is easier to remember.  For example, I find it easier to use a for loop to compile multiple files compared to the magic variables in makefiles.  From now on, however, I will be compiling using makefiles, especially since it is easy once you have written one to change it to match the current project.

**Activity 02: Disk Usage**

*1)* (a) To parse the command line arguments, I used getopts within a while loop.  The syntax is as follows:

	while getopts "an:" option; do

And then it had a case statement on the option variable.  The colon after n indicates that a value will be passed by the user, and thus I changed a variable with the number of entries to show to whatever number was inputted using the $OPTARG value.  Also, if -a was placed, I set the FILES variable to 1, indicating true.  If an invalid flag was inputted (tested using the wildcard), I outputted the correct usage of the command and exitted with a nonzero exit status.

(b) When there were no command line arguments, this getopts while loop would not run. I declared 2 variables, FILES and HEAD, which have the values of 0 and 10 respectively and are the default values, 0 meaning not to show files and 10 meaning show 10 entries.  If there was an invalid input, I outputted the correct usage as discussed in a.  
In the case where there were no directories specified, I checked this by shifting past the flags and looking what came after (see part c).  If there was nothing her, ("$1" = ""), then I stated that there was no directory specfied and exited with a nonzero exit status, listing the correct usage.

(c) To first get the arguments to the front of the line using the $# notation, I used shift on $OPTIND to make the first directory $1, as such:

	shift $(($OPTIND - 1))

I then used a while loop that runs until the command is empty, shifting it to the right each time using shift.  Within this while loop, I had a if statement to check whether the user specified to include files.  The following is the usage for the case where the user specified files:

	 du -a -h $1 2> /dev/null | sort -rh | head -n $HEAD

And the else for this is the exact same with the -a removed.  This takes the human readable sizes of the directories and ouputs the errors to the black hole, piping to sort which sorts by size going from high to low, and then I piped that to head which only displays the top N directories by size, as specified by the user or defaulting to 0.

(d) As above, I used the if statement to determine whether or not to include files.  This ran if $FILES was equal to 1, which was the case if the user put -a as an option.  I also used -n $HEAD in displaying the top commands, and this givesn the top N options as specified by the user or defaulting to 10 as declared in the beginning.

*2)* The hardest part of this script for me was getting the piping with sort and head to work correctly.  For a stupid reason too, as -h in sort does not work on my mac so that took a long time to figure out.  Also, specifying that the sizees should be in human readable size, sorted in reverse by this human readable size, and then take the N top entries, was nontrivial and took a little bit.
Suprisingly, the largest amount of code for a specific purpose was parsing the command line arguments.  This is not too surprising once I think about it, because you need to deal with each flag specified differently, the case where there is an invalid flag entered, the case where no flags are entered, and shifting past these flags.  Not terribly difficult, just a lot.

**Activity 03: Taunt**

*1)* (a) To handle different signals, I used the trap command.  Trap executes the command preceding the signal recieved as specified. The following is one example:

	trap password SIGHUP

Thus, if the SIGHUP signal is received, the script will run the password function, which has its own message using cowsay and a here script that will be discussed in b.  Likewise, if I trapped the signals SIGINT or SIGINT, I ran the function taunt, which had its own message.

(b) To pass long messages to cowsay, I used a here script.  This is a form of I/O redireciton that allows me to send a few lines of text ending with the EOF command. The syntax I used was as follows:

	/afs/nd.edu/user15/pbui/pub/bin/cowsay -d -f head-in <<-EOF

Which passes all of the text to cowsay until EOF is typed.  This was the main constituent of my functions taunt and password, and I only used one-liners for the other two commands.  

(c) To deal with the timeout, I first declared two variables, an iterator and a max number.  I used a while loop that runs while the iterator is less than the declared max number.  Every time the while loop runs, I sleep for one second and iterate the iterator.  Thus, by default the while loop will run ten times for ten seconds, and if at any point it receives SIGHUP, SIGINT, or SIGTERM, it will display the function and end the program.  If the while loop succeeds with no correct signals sent, it will display a message using cowsay that states that he is going back to sleep.

*2)* For me, I believe that C programs are easier to use. Little things like the space that must be inbetween if, [, and the inside value are annoying and can sometimes be hard to diagnose.  I much prefer C program, but of course they are used for very different things.  One advantage to shell scripting syntax that I noticed is that for loops and variables are easier to declare and use, but you have more control over this in C programs.
	Shell scripts are much more prefered when you want to use commands specific to the command line, such as to manipulate directories or use networking commands.  C programs are entirely different, and are much prefered when doing any computation, creating games, or performing any task that does not need the command line.
