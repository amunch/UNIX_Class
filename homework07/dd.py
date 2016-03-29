#!/usr/bin/env python2.7
#By: Andy Munch
#Worked with Mark Pruitt

import getopt
import os
import sys

#Global Variables

IF=0
OF=1
COUNT=sys.maxint
BS=512
SEEK=0
SKIP=0

PROGRAM_NAME = os.path.basename(sys.argv[0])

def error(message, exit_code=1):
	print >>sys.stderr, message	
	sys.exit(exit_code)

def usage(exit_code=0):
	error('''Usage: {} options...

Options:

	if=FILE     Read from FILE instead of stdin
	of=FILE     Write to FILE instead of stdout

	count=N     Copy only N input blocks
	bs=BYTES    Read and write up to BYTES bytes at a time

	seek=N      Skip N obs-sized blocks at start of output	
	skip=N      Skip N ibs-sized blocks at start of input'''
	.format(PROGRAM_NAME), exit_code)


def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
        print >>sys.stderr, 'Could not open file {}: {}'.format(path, e)
        sys.exit(1)

def read_fd(fd, n):
    try:
        return os.read(fd, n)
    except OSError as e:
        error('Could not read {} bytes from FD {}: {}'.format(n, fd, e))

def write_fd(fd, data):
    try:
        return os.write(fd, data)
    except OSError as e:
        error('Could not write {} bytes from FD {}: {}'.format(len(data), fd, e))

ARG = sys.argv[1:]

split_list = []

for argument in ARG:
	split_list.append(argument.split('='))

for element in split_list:
	if element[0] == 'if':
		IF = element[1]		
	elif element[0] == 'of':
		OF = element[1]
	elif element[0] == 'count':
		COUNT = element[1]
	elif element[0] == 'bs':
		BS = element[1]
	elif element[0] == 'seek':
		SEEK = element[1]
	elif element[0] == 'skip':
		SKIP = element[1]
	else:
		usage(1)
		error('Invalid command line argument', 1)
	
if IF is not 0:
	fd = open_fd(IF, os.O_RDONLY)
else:
	fd = 0

if OF is not 1:
	target = open_fd(OF, os.O_WRONLY|os.O_CREAT)
else:	
	target = 1

NUM = 0

if IF is not 0:
	os.lseek(fd, int(SKIP)*int(BS), 0)
if OF is not 1:
	os.lseek(target, int(SEEK)*int(BS), 0) 

data = read_fd(fd, int(BS))
while data and NUM < int(COUNT):
	write_fd(target, data)
	data = read_fd(fd, int(BS))
	NUM += 1

os.close(fd)
os.close(target)
