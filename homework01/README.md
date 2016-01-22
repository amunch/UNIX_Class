Homework 01
===========

**Exercise 1**

*1.* To navigate to the csesoft AFS directory using an absolute path, type the following:

	$ cd /afs/nd.edu/user14/csesoft

*2.* We are in our AFS home directory, located at /afs/nd.edu/user14/amunch.  To get to csesoft, we need to go back two directories from our current directory, then go to user14 and csesoft.  Use the following command:

	$ cd ../csesoft

*3.* As above, go to home directory, then down a level, then to csesoft, as shown:

	$ cd ~/../csesoft

*4.* To create a symbolic link in my Home directory, use the ln -s operation.

	$ ln -s /afs/nd.edu/user14/csesoft csesoft

**Exercise 2**

*1.* Use the cp command, along with the -r option.  The r option ensures that all folders within the pixmaps folder will also be copied over with their contents.  Also, after pixmaps, place * so that everthing is copied.

	$ cp -r /usr/share/pixmaps/* images

*2.* Broken links are in red text and highlighted in black.  They cannot be accessed. To get a list of what links are broken, use the following command:

	$ find . -xtype l

*3.* Use the mv command to move the contents of a directory to a new directory of a different name:

	$ mv images pixmaps

This operation took .01 s, as it simply renamed the folder.

*4.* To move the pixmaps folder to the temp directory, use the following command similar to 3:
	
	$ mv pixmaps /tmp/amunch-pixmaps

This operation took 6.3 seconds, as it actually had to copy all of the files to a different directory.

*5.* To delete the pixmaps folder, use rm with the -r command to remove the entire directory as follows:

	$ rm -r /tmp/amunch-pixmaps

This took .03 seconds, as it was a simple delete operation.

**Exercise 3**

*1.* To long list the directory in the human readable format, use ls with the -lh options, using l for the long list and h for the human readable format:

	$ ls -lh /afs/nd.edu/user37/ccl/software

*2.* To long list ordered by time from newest to oldest, use the -lt options, where t orders it by time:

	$ ls -lt /afs/nd.edu/user37/ccl/software

*3.* 


**Exercise 4**

*1.* The following is the permissions for data.txt:
	
	rwxr-x--x

This indicates that the owner has read, write, and execution permission.  The group assigned to this file has read and execution permission.  Everyone else has execution permissions.

*2* The following will give the specified permissions.
*a.* Only you can read and write to the file:
	
	$ chmod 500 data.txt

*b.* Only you and members of your group can read, write, and execute the file: 

	$ chmod 770 data.txt

*c.* Anyone can read the file:

	$ chmod 444 data.txt

*d.* There are no permissions on the file:

	$ chmod 000 data.txt

*3* The owner is still allowed to delete the file, but the command line warns the user that the file is write protected, and the user must type yes to continue the delete process.

**Exercise 5**

*1* In the home directory, the administrators and the owner have all of the permissions: lookup, insert, delete, administer, read, write, and lock.  Other users on campus and others in the group only have lookup permissions.  For the private directory, the administrator and owner permissions are retained, but the lookup permissions of the campus and the group are removed.  For the public directory, the permissions are slightly more than fror the home directory, with some additional permission for the campus and group including read and lock permissions.


