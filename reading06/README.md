Reading 06
==========

**1.** To convert all the inputted text to upper case, use the trace command.  You must put both lower and upper after trace to tell it to convert all lowercase letters to uppercase, and lower and upper must be in double quotes to indicate that it is a string:

	$ echo "All your base are belong to us" | tr "[:lower:]" "[:upper:]"

**2.** To find the shell of the root user, I first used cat on the etc/passwd to output its contents to stdout.  To find the line the specifies the shell, I then used grep on root and bin.  Then, I used the cut command on this line using the delimiter : and selecting the seventh field as this is where this directory is specified.

	$ cat /etc/passwd | grep root:/bin | cut -d':' -f7

**3.** To find and replace all instances of a word, first echo a line and pipe it into the sed command.  Then, using the form 's/old_word/new_word/', specify the words you would like to replace and replace them with your desired word:

	$ echo "monkeys love bananas" | sed 's/monkeys/gorillaz/'

**4.** As with above, I used the sed command to replace all instances of the text, using ; to specify more than one.  I then used grep on python to examine the changes I made.  I had to use \ before every forward slash within sed to indicate that it was a special character:

	$ cat /etc/passwd | sed 's/\/bin\/bash/\/usr\/bin\/python/;s/\/bin\/csh/\/usr\/bin\/python/;s/\/bin\/tcsh/\/usr\/bin\/python/' | grep python

**5.** To remove, the leading whitespaces, again use sed but this time replace it with nothing.  The options in the second part of the replace command delete both the space and the tabs, just in case the leading whitespace was a tab:

	$ echo "     monkeys love bananas" | sed 's/^[ \t]*//'

**6.** To find the records that have a field beginning with a 4 and ending with a 7, I used grep and a grep exception.  I first grepped for :4, which gave me any and all fields starting with 4.  Within this, I also accepted any characters after except :, which would mean the field only contained 4.  I then grepped for 7:, to get all the fields that ended in 7:
	
	$ cat /etc/passwd | grep ":4[^:]" | grep "7:"

**7.** To follow the output of a file as it grows, use the tail -f command.  For example on the log file /var/log/wtmp/, use the following command:

	$ tail -f /var/log/wtmp

**8.** To show all the lines that are present in two files, use comm.  Also, use the flags -12 to suppress the output of unique lines of each of the files.  For two files hello.c and hey.c:

	$ comm -12 hello.c hey.c
 
