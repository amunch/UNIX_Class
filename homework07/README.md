Homework 07
===========

*dd.py*

**1)** To parse the command line options, I first got a list of all the argument using sys.argv[1:], which returned everything after the program name.  I then split it using the split function based on the equals sign, which gave me the the option and what the user set that option to for each argument as such:

	split_list.append(argument.split('='))

I then looped through all of the elements using a for loop, as the list was now a list of doubles, where the zeroth element is the option and the first element is the value.  If the element option did not match any of the options, I outputted the usage and ended the program.

**2)** I opened a file using an open_fd function, which returned a file object using the os.open function.  If this was not successful, I printed an error and exited the program. If IF was set to a different value, I opened it as os.O_RDONLY, as we are simply reading from the input file and do not want to mess with it in any other way.  If OF was not equal to the default 1, I opened it using the os.O_WRONLY mode, and os.O_CREAT if the file did not exist.  That way we can write our output to the file.
	If IF was its default value of 0, I set fd to be 0, and this will indicate to use stdin.  If OF was its default value of 1, I set target, the target file object, to be 1 and this will indicate to write to stdout.

**3)** Seek and skip can only be used if the input or output file are not stdin or stdout, respectively. If this is not the case, I used os.lseek on the file object, and multiplied skip by the block size to see how many bytes to skip.  Of course, if one of these is 0, as skip is by default, it will remain at the beginning of the file.  If not, it will set the position within the file object to be where it is desired.
	Similarly, I used os.lseek on the target file in the same manner, and this will start writing to the file where how many bytes the user specified to skip.

**4)** Count specifies how many blocks to copy, so I used a counter that incremented by 1 every time and exitted the copy loop if it exceeded count. Also, this loop used the value while data, which remains true when the end of the file has not been reached.
	Within the loop, I read a chunk of data of size BS, and wrote this to the output file.  Thus, the counter counts how many times a size of BS has been read and continues reading until this either becomes less than COUNT or EOF is reached.

*find.py*

**1)** 
