Homework 05
===========

**1.**
*a)* To construct the source set, I first hardcoded both the lower and uppercase alphabet in alphabetical order.  I then concatenated these strings using the following command, and this gave me my source set:

	SET1=$UPPER$lower

*b)* First, it is worth mentioning that I made the numbers over 26 work by using the modulus, where the remainder with 26 is the number we will shift to the right by:
	
	NUM=`expr $NUM % 26`
	
To construct the target set, I had to create 4 different strings.  The first cut out everthing before and including the n'th character as such:
	
	SHIFTUP1=$(echo $UPPER | cut -b `expr $NUM + 1`-26)

This took all bits not including n and on.  The same thing was done for the string of lower characters.
To get back all of the characters that were not in this shift, I just cut out anything that was not the first to n'th bit as such, for both upper and lower:

	SHIFTUP2=$(echo $UPPER | cut -b 1-$NUM)

I then concatenated as such:

	SET2=$SHIFTUP1$SHIFTUP2$shiftlow1$shiftlow2

So we had the shifted bits first and the rest after, and as with SET1, we used the upper case letters first and then the lower case letters.

*c)* To perform the encryption, I used the translate command:

	tr $SET1 $SET2

This took the letters from the first, normal set and replaced them with numbers from the second, shifted set.  It returns our translation.

**2.** 
*a)* The following is the (long) command that I used to only extract the relevant portions of the data:

	curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | grep -v redditmedia | cut -d '"' -f4 | grep -v '&lt' | grep -v embed | head -n $HEAD

The curl command fetches the json data for the specified subreddit (stored in $1 as I did a shift on the arguments) and puts it through the python script to extract it stdout.  I then greped for the term url as these are the links for the page, and removed the redditmedia links because these are just junk (I suspect ads).  I then cut out everything but the fourth field using the " delimiter, as this is how the data is stored.  I then removed the terms with &lt and embed, as these were more junk that were showing up in different subreddits. I then took the top amount of links as specified by the user, defaulting to 10, using head -n.

*b)* To manage the different operations, the above command was what I used for the default, no options, command.  There was a variable I used called choice which was set to 1 if the user wanted to shuffle and 2 if the user wanted to sort.  I dealt with this using an if statement to see if CHOICE had either of these options, and if not it used an else to default to the command in a.  For shuffle, I simply added a shuf after the cut command in a.  For sort, I simply piped it through sort after the cut in a.

*c)* If only one flag was added in the command, the CHOICE variable got its variable and it went through the if statement.  If two were inputted, using getopts will simply overwrite the CHOICE variable the second time around, and since we want the last flag this works.  This is why I used the same variable.  If any illegal flags were inputted or no subreddits were specified, I used a here document to write the correct usage.  I then shifted to the first argument, and thus this would be stored in $1.

**3.**
*a)* To remove comments, I used the following command:

	sed -r "s|$DELIM.*||g"

Here I replaced the delimter and everything after it with nothing, so it is a now a blank line.  g indicates that this is done globally in the line.  Also, I used | as a delimiter because C++ comments have the same delimiter as sed, \.  No biggie.  Also, this was before the remove empty line command, as this itself will output an empty line.

*b)* to remove empty lines, I used the following:

	sed '/^$/d'

^$ works because this defines a line that ends immediately after it begins, a blank line, so this line deletes that.

*c)* If the user used the -d flag, I used getopts and set DELIM to OPTARG, the value inputted by the user.  If the user specified the -W flag, I set the STRIP variable to 0, and simply removed the command from b. I achieved this by using an if statement that runs all three seds if the -W flag was not defined and only the ones that delete the comments and trailing whitespace if the -W flag was specified.  If any command line options did not match this, then I displayed a usage screen and exitted.
