TLDR - Shell Scripting
======================

**Variables** - Variables are assigned using the '=' operator, and there must be no spaces in between the variable name, the operator, and the value:
	
	VAR=1
	title="This is how Shell Scripts work"

**Capturing STDOUT** - The output of a script can be captureed using the '>' operator.  For example, the output of a script that creates an HTML file can be captured as such:

	./my_html > my_html.html

**If statements** - It is very important that if statements are syntactically correct.  Otherwise, they behave the same as any if statement.  You must end the if statement with fi.  The following returns links that are symbolic:

	if[ -L $i ]; then
		echo $i
	fi

The following shows the use of else:

	if[ -L $i ]; then
		echo $i
	else
		echo "No Match"
	fi

**Case statements** have similar behavior to any other case statement, by each case must end with ;; and the case statement must end with esac:

	case $i in
		1 ) echo "You input 1."
			;;
		2 ) echo "You input 2."
			;;
		3 ) echo "You input 3."
			;;
	esac

You can also add a defualt statement by using the wildcard operator:

		* ) echo "There was no match."

**For loops** take in a variable and loop through all of the available values.  It uses the in word as the iterator, and do to tell the loop what commands to execute for every value:

	for i in words; do
		echo $i
	done

**While loops** execute a sequence of commands while the truth value within the brackets is 1.  Again, syntax is very important, especially putting spaces between the brackets and the value to be evaluated for truthfulness. 

	num=0
	while [ $num -lt 5 ]; do
		echo $num
		num=$((num+1))
	done

**Functions** are similar to functions in any other programming language.  The following is a simple function to return the name of a machine:

	sys_name()
	{
		name=`uname`
		echo $name
	}

And in the main body of the function, simply call the function:

	$(sys_name())

**Trap** executes a given command when a specified signal is received by the script.  You give trap a list of signals and a command (arg), written in the following way:
	
	trap arg signals

An example of this prints that a signal was received whan hangup or interrupt was receieved by the script:

	trap "echo "signal received"; exit" SIGHUP SIGINT
