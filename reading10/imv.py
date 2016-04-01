#!/usr/bin/env python2.7
#By: Andy Munch

import getopt
import os
import sys
import tempfile

#Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])

def error(message, exit_code=1):
	print >>sys.stderr, message	
	sys.exit(exit_code)

def usage(exit_code=0):
	error('Usage: {} FILES...'.format(PROGRAM_NAME), exit_code)
	sys.exit(status)

def open_fd(path, mode): #Try to open the file.
    try:
        return os.open(path, mode)
    except OSError as e:
        print >>sys.stderr, 'Could not open file {}: {}'.format(path, e)
        sys.exit(1)

try: #Handle the command line arguments.
	opts, args = getopt.getopt(sys.argv[1:], "h")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts: #If there any options, print usage.
	usage(1)

if len(args) == 0: #If there are no files, print usage.
	print "Please specify a command"
	usage(1)

PATHS = tempfile.NamedTemporaryFile(delete=False) #Create temporary file in /tmp/

for argument in args: #Write the files to the temporary file.
	PATHS.write(argument)
	PATHS.write("\n")	

PATHS.close() #Close the file to be editted by the user.

SEQ = ["${EDITOR:-nano}", PATHS.name] #Create command, default to nano.
SPACE = ' '
COMMAND = SPACE.join(SEQ)

try: #Try to open the editor, print errors if they occur.
	os.system(COMMAND)
	EDITTED = []
except OSError as e:
	print >>sys.stderr, 'Unable to open editor:{}'.format(e)
	sys.exit(1)

f = open(PATHS.name, "r") #Open file readonly.
for line in f:
	EDITTED.append(line.rstrip()) #Create a list of editted files.

ZIPPED = zip(args, EDITTED) #Create a list of lists for easy comparison
try:
	for element in ZIPPED: #try to rename.  If this is not possible, print errors.
		print element
		os.rename(element[0], element[1])
except OSError as e:
	print >>sys.stderr, 'Unable to rename file:{}'.format(e)
	sys.exit(1)

PATHS.close() #Close file, delete, and exit the program
os.unlink(PATHS.name)
sys.exit(0)
