Homework 02
===========

**Activity 1**

*1.* 

	# Create a workspace on my chosen source machine, student105. Unix will replace ${USER} with the name of the current user.
	$ mkdir /tmp/${USER}-workspace

	# Generate 10MB file with data from /dev/urandom as the input.  I output to a file called 10MB.  The amount in bytes is 10M, or 10MB. This command assumes you are in the /tmp/${USER}-workspace
	$ dd if=/dev/urandom of=10MB bs=10M count=1

	# Create 10 hard links to the 10MB file we just create.
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data0
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data1
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data2
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data3
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data4
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data5
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data6
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data7
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data8
	$ ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data9

	# Create workspace on target machine.  In this case, I ssh'ed into the remote106 machine and ran the same command as in the first part.
	$ mkdir /tmp/${USER}-workspace



**Activity 2**

*1.* Scan 'xavier.h4x0r.space' for HTTP port. The -v option updates the output as nmap works to map the network.  The -Np option skips DNS lookup, which caused the server to be seen as not available:

	$ nmap -v -Pn xavier.h4x0r.space

This gave two ports available inthe 9000-10000 range:

	9111/tcp open  DragonIDSConsole
	9876/tcp open  sd

To see which one is the right HTTP port, I curled it, using:

	$ curl xavier.h4x0r.space:9111 

	$ curl xavier.h4x0r.space:9876

Which led me to port 9876 as the next step.

*2.* Curl not only allowed me to tell which port was right, but also accesses the server.  Using:
	
	$ curl xavier.h4x0r.space:9876

I got the following output:

	 _________________________________________ 
	/ Halt! Who goes there?                   \
	|                                         |
	| If you seek the ORACLE, you must query  |
	| the DOORMAN at /{netid}/{passcode}!     |
	|                                         |
	| To retrieve your passcode you must      |
	| decode the file at                      |
	| ~pbui/pub/oracle/${USER}/code using the |
	| BASE64 command.                         |
	|                                         |
	\ Good luck!                              /
	 ----------------------------------------- 
	     \
	      \  (__)  
 	         (\/)  
	  /-------\/    
     	 / | 666 ||    
	*  ||----||      
	   ~~    ~~      

*3* To decode my passcode, I used the base64 command with the -d option in order to decode it:

	$ base64 -d ~pbui/pub/oracle/${USER}/code

Which output my code:

	a6bcc98ef95a44e9b6ed8a3348bc01aa

*4.* To send the passcode, I queried port 9876 at my netid and passcode:

	$ curl xavier.h4x0r.space:9876/amunch/a6bcc98ef95a44e9b6ed8a3348bc01aa

This returned the following directions:

	~pbui/pub/oracle/SLEEPER

Where I have to signal the SLEEPER to hangup his connection.

*5.* To signal the sleeper to hangup, we have to use the pkill command.  This is best done using two windows logged into the same machine.  In one window I run the SLEEPER:

	$ ~pbui/pub/oracle/SLEEPER

In the second window, I kill it with pkill, sending the code 1 to signal it to hangup:

	$ pkill -1 ~pbui/pub/oracle/SLEEPER

This returned the following code from the SLEEPER:

	bnpoYXB1PTE0NTQxMDU3MDQ=

Which I will use to talk to the Oracle.

*6.* To talk to the oracle, I use telnet on the other port, entering my name and passcode given to me by the sleeper.

	$ telnet xavier.h4x0r.space 9111

And there it is.

