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
		CHARACTER = True
	elif o == '-l':
		NEWLINE = True
	elif o == '-w':
		WORD = True
	else:
		usage(1)

EXPLICIT = True

if len(args) == 0:
	args.append('-')
	EXPLICIT = False

ARGUMENT = ''

for path in args:
	if path == '-':
		stream = sys.stdin
		ARGUMENT = path
	else:
		stream = open(path)
		ARGUMENT = path

SUM = 0

if CHARACTER == True:
	for char in stream:
		SUM += len(char)
	if ARGUMENT == '' or EXPLICIT == False:
		print SUM
	else:
		print SUM, (ARGUMENT)
elif NEWLINE == True:
	for line in stream:
		SUM += 1
	if ARGUMENT == '' or EXPLICIT == False:
                print SUM
        else:
                print SUM, (ARGUMENT)
elif WORD == True:
	for line in stream:
		SUM += len(line.split())
	if ARGUMENT == '' or EXPLICIT == False:
                print SUM
        else:
                print SUM, (ARGUMENT)

stream.close()
