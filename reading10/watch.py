#!/usr/bin/env python2.7
#By: Andy Munch

import getopt
import os
import sys
import time

#Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
INTERVAL = 2

def error(message, exit_code=1):
	print >>sys.stderr, message	
	sys.exit(exit_code)

def usage(exit_code=0):
	error('''Usage: {} [-n INTERVAL] COMMAND

Options:
	
	-n INTERVAL   Specify update interval (in seconds)'''.format(PROGRAM_NAME), exit_code)
	sys.exit(status)

try:
	opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == '-n':
		INTERVAL = a
	else:	 
		usage(1)

if len(args) == 0:
	print "Please specify a command"
	usage(1)

SPACE = ' ' 
COMMAND = SPACE.join(args)

while(1):
	try:
		os.system('clear')
		print 'Every {0}s: {1}'.format(float(INTERVAL), COMMAND)
		os.system(COMMAND)
		time.sleep(float(INTERVAL))
	except KeyboardInterrupt:
		sys.exit(0)
