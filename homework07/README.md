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

**1)** Parsing the command line options was done by first getting a list using the sys.argv command, taking the third argument and on.  I then implemented a count that will be at the current argument.  While this count is less than the length of the argument list, I ran a loop that set all of the values based on user inputs.  If the specific argument required a value that is the next value in the list, I incremented the count and then set the corresponding value to that element.  After each loop, I incremented count to go to the next argument.  If any arguments were not in the list, I showed the usage screen and exitted.

**2)** To walk the directory tree, I created a walk function.  This function attempts to return a 3-tuple of the root, files, and directories using the os.walk command. This command sets topdown to be true and followlinks to be true, so that it will start from the specified path and work its way down, and also follow all symbolic links.  If there was an error, it prints the error and exits.  If this successfully returned the 3-tuple, which is looped through and includes files or directories based on if it passes the include function.

**3)** The main method of determining whether to include a object's path was the include function.First, if the executable option was specified, I called an is_exe function to determine if the file is exectuable.  This was done by using the os.path.exists command on the path and os.access with the os.X_OK mode.  If either of these was false, inclue returned false and this path was not included.  The same thing was done for READABLE and WRITABLE, except that the mode os.R_OK was used for READABLE and os.W_OK was used for WRITABLE.
	If the empty option was set to true, the function determined if the path was a directory, a file, or a symlink.  Symlinks were always false considered empty.
