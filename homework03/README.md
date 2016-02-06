Homework 03
===========
*Activity 1*
*Task 2 Questions*  

**1.** 

**a.** libgcd.so is larger than libgcd.a. This is because a shared library is executable, whereas a static library is compiled and linked directly within the program.  Shared libraries are loaded at application time to the program using these libraries.

**b.** gcd-static is much larger than its dynamically linked brother as it contains all of the libraries within it.  gcd-dynamic merely links to the libraries, and thus is much smaller.

**2.** gcd-static does not depend on libraries at runtime, as they are baked into the binary of the executable.  gcd-dynamic depends on linux-vdso.so.1, libgcd.so, libc.so.6, and /lib64/ld-linux-x86-64.so.2.  To find this information, I used the following command:
	
	$ ldd ./gcd_dynamic

And when run on static, it returns nothing as static has no dependent libraries.

**3.** It does not work, as does not know where the shared library libgcd.so is.  This was also noted when running ldd, as it returned "not found" for that library.  To allow gcd-dynamic to work, set the environmental variable LD_LIBARARY_PATH to ., which was successful in getting gcd-dynamic to work:

	setenv LD_LIBRARY_PATH .

**4.** The advantage to staticly linked libraries are that the libraries are all in the binary, there is no need to make sure that running on another machine has the necessary libraries.  The advantage to dynamically linked libraries is that the executables are smaller.  
	If I were creating an application, I would by default produce dynamically linked libraries as the size benefits are substantial.  In the case I am using a non-standard library, sure I would statically link the library, but I do not think that this usage case is prevalent enough to default to static linking every time. 

*Activity 2*
*Task 3: Questions*

**1.** To get the archive, I used the wget command to download the .tar from the given link.  The following command was used:

	$ wget https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is_palindrome.tar.gz

To extract the archive, I used the tar command with the appropriate flags:

	$ tar -xvf is_palindrome.tar.gz

Which extracted the files in the archive into a directory called is_palindrome.

**2.** -g forces gcc to inlude debugging symbols in the executable.  This increases the size of the executable by a little less than 50%, where without debugging symobls it was 7.9K :
	
	-rwxr-xr-x 1 amunch dip 7.9K Feb  5 20:01

and after it was 11K :

	-rwxr-xr-x 1 amunch dip  11K Feb  5 20:02

**3.** To find the segmentation fault, I used gdb and narrowed it down to the fgets command, and eventually noticed something was wrong with the buffer.  To find this, I used the following:

	$ gdb is_palindrome
	(gdb) run
	//Enter a random string of letters.

Which returned a seg fault.  To find where exactly this occurred, I used the following:

	(gdb) backtrace

To diagnose the invalid memory access issue, I used valgrind with the following options:

	$ valgrind --tool=memcheck --leak-check=yes --track-origins=yes is_palindrome

Which also gave me the location of a few memory leaks.  The track origins flag allowed me to trace the memory access issue to the is_palindrome function, where I noticed the back pointer was overshooting the last character.  To fix this, I simply subtracted 1.  In addition, valgrind was giving me weird issues with the malloc done for sanitized in sanitize_string, and assigning strdup(s) to this fixed it right up.
	The memory leaks were noticed when running valgrind again.  strdup allocates memory, and this needs to be freed.  Since sanitized changes every loop in main, I needed to free sanitized after the result assignment within the loop.  Once this was done, no errors occurred and the program runs perfectly.

**4.** The most difficult bug to find was definitely the memory leaks.  I had freed sanitize outside of the loop, but this of course still led to memory being allocated and not freed as the loop kept redefining sanitize.  It was difficult because valgrind kept telling me that it was sanitize, but I already freed this, unfortunately outside the loop.
	To prevent future bugs like this, always make sure to free memory every time it is allocated especially in loops.


*Activity 03*

**1.** Contacting the 'COURIER':
	
	$ /afs/nd.edu/user15/pbui/pub/bin/COURIER

He had the following message:

	Hmm... you sure you put the package in the right place?    

**2.** To find the package location, I suspected that the COURIER was using stat to determine the status of certain file locations.  Using strace to find all stat system calls, I noticed a certain loaction that seemed suspicious.

	$ strace -e stat /afs/nd.edu/user15/pbui/pub/bin/COURIER   

returned all stat system calls, including:

	stat("/tmp/amunch.deaddrop", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0

So I made this file:

	touch /tmp/amunch.deaddrop

**3.** Talking to the COURIER again, it said:

	Whoa whoa... you can't give everyone access to the package! Lock it down!

So i have to change the permissions. To do this use chmod:

	chmod 700 /tmp/amunch.deaddrop

Now, the COURIER says 

	What are you trying to pull here? The package is the wrong size!    

I'll investigate further (there is nothing in my directory).

**4.** Seeing all of the read calls to see what the COURIER is looking for:

	$ strace -e read /afs/nd.edu/user15/pbui/pub/bin/COURIER

I came across this line:

	\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0p\356!\377=\0\0\0

I figured that the COURIER was looking for this line in the deaddrop, so i copied it into my deaddrop and talking to the COURIER it looks good:

	Well, everything looks good... I'm not sure what '\177ELF\' means, but I'll pass it on. 


