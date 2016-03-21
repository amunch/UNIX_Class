#!/usr/bin/env python2.7
#Implementation of the wc command using Python
#By: Andy Munch 

import getopt
import sys
import os
import string

CHARACTER = False
NEWLINE = False
WORD = False

def usage(status=0):
	print '''usage: wc.py [-c -l -w] files ...

	-c	print the byte/character counts
	-l 	print the newline counts
	-w	print the word counts'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

try:
	opts, args = getopt.getopt(sys.argv[1:], "clw")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == '-c':
		CHARACTER
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
