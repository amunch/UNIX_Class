#!/usr/bin/env python2.7
#Implementation of the cut command using Python
#By: Andy Munch 

import getopt
import sys
import os
import string

DELIM = '\t'

def usage(status=0):
	print '''usage: wc.py [-d DELIM -f] files ...

	-d DELIM  use DELIM instead of TAB for field delimiter
	-f FIELDS select only these FIELDS'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

try:
	opts, args = getopt.getopt(sys.argv[1:], "d:f:")
except getopt.GetoptError as e:
	print e
	usage(1)

FIELDS = []

for o, a in opts:
	if o == '-d':
		DELIM = a
	elif o == '-f':
		FIELDS = a.split(',')
	else:
		usage(1)

if len(FIELDS) == 0:
	print "Please specify a field."
	sys.exit()

if len(args) == 0:
	args.append('-')


for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

array = []
count = 0

for line in stream:
	array = line.split(DELIM)
	for num in FIELDS:
		count += 1
		sys.stdout.write(array[int(num) - 1].rstrip())
		if count is not len(FIELDS):
			sys.stdout.write(':')
	count = 0
	sys.stdout.write('\n')

stream.close()
