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

*2.* The total disk usage is found running the du -h command, to list the size of the directory in a human readable format, of course logged onto the source machine:

	$ du -h /tmp/${USER}-workspace

which gives the following ouput:

	11M	/tmp/amunch-workspace

Indicating that the size is 11MB, which is not suprising at all because hard links are basically copies of the source file.  There is some overhead but this is close enough.

*3.* Using the du command for the size of the directory:

	$ du -h /tmp/${USER}-workspace

I get the following output:

	11M	/tmp/amunch-workspace

This is expected to be the same as 2, as scp and sftp will just overwrite files of the same name, and rsync does not copy files that are already there.

*4.* 
	# Transfer data files using scp.  Use the * to indicate that I want to transfer all files.
	$ scp /tmp/${USER}-workspace/* amunch@remote106.helios.nd.edu:/tmp/${USER}-workspace
	# I was then prompted to enter the passwords for both and then a progress bar was shown for each file, indicating their progress.

	# Transfer data files using sftp.  First I need to create a file, called in, on the target computer with the follwoing line:
	$ get /tmp/amunch-workspace/* /tmp/amunch-workspace
	# Next, I need to go to the target machine and type the following as the command:
	$ sftp amunch@remote105.helios.nd.edu < in
	# This will connect to the source machine, and use the text in the file in to run the desired command in a single line(excluding passwords).

	# Transfer data files using rsync.  rsync uses the same syntax as scp, but does not by default output anything.  I added --stats to get statistics on the transfer:
	$ rsync --stats /tmp/${USER}-workspace/* amunch@remote106.helios.nd.edu:/tmp/${USER}-workspace
	# The output for rsync is a little different.  It tells how many bytes were sent and what files were matched, as rsync does not send data that is already there.

*5.* scp and sftp transfer the files every time it is called, regardless of what is in the target folder already.  When rsync is used multiple times, it is only transferred once, as it matches what is already in the target folder to what is sending and does not send the duplicates.  This saves bandwidth and time for large file transfers.

*6.* I prefer rsync, with the --stats option of course.  I feel that not transferring every single file every time is immensely more useful when it comes to large projects and file transfers.

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

