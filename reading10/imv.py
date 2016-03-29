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

def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
        print >>sys.stderr, 'Could not open file {}: {}'.format(path, e)
        sys.exit(1)

try:
	opts, args = getopt.getopt(sys.argv[1:], "h")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	usage(1)

if len(args) == 0:
	print "Please specify a command"
	usage(1)

PATHS = tempfile.NamedTemporaryFile(delete=False)

for argument in args:
	PATHS.write(argument)
	PATHS.write("\n")	

PATHS.close()

SEQ = ["$EDITOR", PATHS.name]
SPACE = ' '
COMMAND = SPACE.join(SEQ)

os.system(COMMAND)
EDITTED = []

f = open(PATHS.name, "r")
for line in f:
	EDITTED.append(line.rstrip())

ZIPPED = zip(args, EDITTED)

for element in ZIPPED:
	print element
	os.rename(element[0], element[1])

PATHS.close()
os.unlink(PATHS.name)
sys.exit(0)
