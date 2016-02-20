Reading 06
==========

**1.** To convert all the inputted text to upper case, use the trace command.  You must put both lower and upper after trace to tell it to convert all lowercase letters to uppercase, and lower and upper must be in double quotes to indicate that it is a string:

	$ echo "All your base are belong to us" | tr "[:lower:]" "[:upper:]"

**2.** To find the shell of the root user, I first used cat on the etc/passwd to output its contents to stdout.  To find the line the specifies the shell, I then used grep on root and bin.  Then, I used the cut command on this line using the delimiter : and selecting the seventh field as this is where this directory is specified.

	$ cat /etc/passwd | grep root:/bin | cut -d':' -f7

**3.** To find and replace all instances of a word, first echo a line and pipe it into the sed command.  Then, using the form 's/old_word/new_word/', specify the words you would like to replace and replace them with your desired word:

	$ echo "monkeys love bananas" | sed 's/monkeys/gorillaz/'

**4.** As with above, I used the sed command to replace all instances of the text, using ; to specify more than one.  I then used grep on python to examine the changes I made:

	$ cat /etc/passwd | sed 's/\/bin\/bash/\/usr\/bin\/python/;s/\/bin\/csh/\/usr\/bin\/python/;s/\/bin\/tcsh/\/usr\/bin\/python/' | grep python

**5.** 
