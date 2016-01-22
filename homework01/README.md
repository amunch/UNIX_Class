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


