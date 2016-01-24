Reading 02
==========

**1.** Use the tee command and pipe it with the uname command to write to a specified file.  The -a option appends the information to the specified file.

	$ uname | tee -a uname.txt

**2.** To get the IP address of the local machine, use the ifconfig command.  Note that this command is located in the /sbin/ directory on student machines:

	$ ifconfig

**3.** To find out what IP addresses are associated with a domain name, use the host command.  For example, for Google:

	$ host www.google.com

**4.** To check if a host is alive, use the ping command.  For example, for Google:

	$ ping www.google.com

**5.** To securely transfer a file between two machines, use the scp command.  The form of this command is the following:

	$ scp username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2

So, for example, to copy a file isprime.c from my lab1 directory to my lab2 directory on a different machine, use the following command: 

	$ scp amunch@remote101:/afs/nd.edu/user14/amunch/cse20211/lab1/isprime.c amunch@remote102:/afs/nd.edu/user14/amunch/cse20211/lab2

**6.** The command to execute a persistent shell session is the following:
	
	$ tmux

To detach from the current session, type the following:

	$ tmux detach

To reattach to the session that you just detached from, execute the following:

	$ tmux attach

**7.** To download a file from a website, use the wget command.  Use the -O option followed by the desired path to the file to specify where the file goes.  The following is an example:

	$ wget -O image.png www.example.com/image.png

**8.** To scan a remote machine to see what ports are open, use the nmap command.  For example, to see the open ports on scanme.nmap.org, use the following:

	$ nmap scanme.nmap.org


