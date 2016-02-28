TLDR - awk
==========

Overview
--------

[awk] is a language that scans and processes an input, allowing the user to perform many tasks including counting the unique instances of a word or what word occurs the most.


Format:

	awk pattern { action }

Examples
--------

*1)* Printing specific fields is similar to what is done when dealing with shell script command line arguments.  You use the $ followed by a number command and this will return the word corresponding to that placement in the file.  For example, to print the first word(s), use the following:
 
	awk 'print $2'

*2)* Controlling the field input separator is useful when fields are separated by something other than whitespace.  To change the symbol the separates the fields, change 'FS' as follows:

	awk 'BEGIN { FS=":"; }'

*3)* BEGIN and END separate commands that execute before anf after a file is processed.  For example, the following will begin by changing the delimiter and then print the second field separated by that delimiter:

	awk 'BEGIN { FS=":"; } END{print $2}'
	
*4)* To use pattern matching, specify the word in between slashes as follows.  The following will print any lines that have 'word' in it.

	awk '/word/ {print $2}'

*5)* NF specifies the number of fields in the file you are passing to awk, and NR keeps the number of records you are currently outputting.  For example, to loop through a file until the end and print those files that match 'word', while also numbering this output, use the following:

	awk '/word/ {for(i=1;i<=NF;i++) print NR $1}'

*6)* Associative arrays can use anything as the name of the position in an array.  For example, array[andy] is okay, and useful.  The following finds all lines that have word in it, places the word after it in an array with an element of that name, and increments that array member.  It then prints the number of unique entries, and this is a useful way for finding the number of unique words in large files.

	'/word/ {array[$2]++} END{for (key in array) count++} END{print "Number Unique:" count}'

Resources
---------

- [man7](http://man7.org/linux/man-pages/man1/gawk.1.html)

[awk]: http://man7.org/linux/man-pages/man1/gawk.1.html
