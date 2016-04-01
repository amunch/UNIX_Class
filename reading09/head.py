#!/usr/bin/env python2.7
#Implementation of the head command using Python
#By: Andy Munch 

import getopt
import sys
import os
import string

NUM = 10

def usage(status=0):
	print '''usage: head.py [-n NUM] files ...

	-n NUM	print the first NUM lines instead of the first 10'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:h")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == '-n':
		NUM = a
	else:
		usage(1)

if len(args) == 0:
	args.append('-')


for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

unique = {}
count = 0;

for line in stream:
	if count == int(NUM):
		sys.exit()
	count += 1
	line = line.rstrip()
	print line
	

stream.close()
