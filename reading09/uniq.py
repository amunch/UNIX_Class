#!/usr/bin/env python2.7
#Implementation of the uniq command using Python
#By: Andy Munch 

import getopt
import sys
import os
import string

PREFIX = False

def usage(status=0):
	print '''usage: uniq.py [-c] files ...

	-c	prefix lines by the number of occurrence'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

try:
	opts, args = getopt.getopt(sys.argv[1:], "ch")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == '-c':
		PREFIX = True
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

for line in stream:
	line = line.rstrip()
	if line not in unique:
		unique[line] = 1
	else:
		unique[line] = unique[line] + 1

if PREFIX == False:
	for x in sorted(unique):
		print (x)	
else:
	for x in sorted(unique):
		str_num = str(unique[x])
		print (str_num.rjust(7)), (x)

stream.close()
