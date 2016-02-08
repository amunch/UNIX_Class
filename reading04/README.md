Reading 04
==========

*1.* To extract the contents of a tar file, use the tar command with -xvf flags. x tells tar to extract, v makes the command verbose, and f uses an archive file.

	$ tar -xvf file.tar.gz

*2.* To compress the contents of a directory, use the tar command with options z to compress, c to create archive, v to display progress, and f for archive file.

	$ tar -zcvf data.tar.gz *location of /data/*

*3.* To extract the contents of a zip file, use the unzip command:

	$ unzip file.zip

*4.* To zip the contents of a directory, use the zip command with -r to zip all of the files and subdirectories within that directory.

	$ zip -r file.zip data

*5.* To install a new package on a Debian-based system, use apt-get.

	$ apt-get install {package}

*6.* To install a package on a Red Hat Linux system, use the yum install command:

	$ yum install {package}

*7.* To install a Python package, use pip, where {package} is a Python package:

	$ pip install {package}

*8.* To paste the contents of a file to the online pastebin sprung, pipe the cat command with curl.

	$ cat {file} | curl -F 'sprunge=<-" http://sprunge.us

Which will return a link that can be used to access this pastebin and share it with others.

*9.* To run commands as the root user, preface the command with sudo.  For example, for ls (haha) use the following:

	$ sudo ls

You will have to enter your password as running commands as the superuser can be dangerous.
