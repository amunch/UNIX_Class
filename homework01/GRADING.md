Homework 01 - Grading
====================

**Score**:  13.25 / 15

Deductions
----------

Exercise 3:
-0.5 (7)
Exercise 4:
-0.25 (2a)
-0.5 (3)
Exercise 5:
-0.5 (2)








Comments
--------

Exercise 3:
(5) You can also do $ du -sh /afs/nd.edu/user37/ccl/software/cctools/x86_64/* | sort -rn
(7) find /afs/nd.edu/user37/ccl/software/cctools/x86_64 -type f | xargs du -h | sort -rh | head
parrot_run or parrot_run_hdfs is the largest at 18M. Your command may have treated 989K as greaterr
than the 18M of parrot_run

Exercise 4:
(2) a. chmod 600 or chmod g-rx,o-x. chmod 500 gives you execute, but not write, permissions
(3) The owner of the directory containing the file, or the root user

Exercise 5:
(2) /afs/nd.edu/common has Unix permissions `drwxrwxrwx`, but we can’t touch a file b/c of AFS ACLs.  This means AFS supersedes or overrides Unix permisions


