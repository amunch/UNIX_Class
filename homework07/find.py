#!/usr/bin/env python2.7
#By: Andy Munch
#Worked with Mark Pruitt

import os
import sys
import stat
import fnmatch
import re
from stat import *

#Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])

DIRECTORY = sys.argv[1]
TYPE = ''
EXECUTABLE = False
READABLE = False
WRITABLE = False
EMPTY = False
NAME = ''
PATH = ''
REGEX = ''
PERM = ''
NEWER = ''
UID = 0
GID = 0

def error(message, exit_code=1):
	print >>sys.stderr, message	
	sys.exit(exit_code)

def usage(exit_code=0):
	error('''Usage: {} options...

Options:

	-type [f|d]     File is of type f for regular file or d for directory

	-executable     File is executable and directories are searchable to user
    	-readable       File readable to user
    	-writable       File is writable to user

    	-empty          File or directory is empty

   	-name  pattern  Base of file name matches shell pattern
    	-path  pattern  Path of file matches shell pattern
    	-regex pattern  Path of file matches regular expression

    	-perm  mode     File's permission bits are exactly mode (octal)
    	-newer file     File was modified more recently than file

    	-uid   n        File's numeric user ID is n
    	-gid   n        File's numeric group ID is n'''
	.format(PROGRAM_NAME), exit_code)

def walk(path):
	try:
		return os.walk(path, topdown = True, followlinks = True)
	except OSError as e:	
		print >>sys.stderr, 'Unable to open file{}:{}'.format(path, e)
		sys.exit(1)

def is_exe(path):
	return os.path.exists(path) and os.access(path, os.X_OK)

def is_read(path):
	return os.path.exists(path) and os.access(path, os.R_OK)

def is_write(path):
	return os.path.exists(path) and os.access(path, os.W_OK)

def include(path):
	if EXECUTABLE:
		if is_exe(path) == False:
			return False
	if READABLE:
		if is_read(path) == False:
			return False
	if WRITABLE:
		if is_write(path) == False:
			return False
	if EMPTY:
		if os.path.isdir(path):
			try:
				if len(os.listdir(path)) != 0:
					return False
			except OSError as e:
				return False
		elif os.path.isfile(path) and os.stat(path).st_size != 0:
			return False
		elif os.path.islink(path):
			return False	
	if NAME:
		if not fnmatch.fnmatch(os.path.basename(path), NAME):
			return False
	if PATH:
		if not fnmatch.fnmatch(path, PATH):
			return False
	if REGEX:
		if not re.search(REGEX, path):
			return False
	if PERM:
		try:
			if oct(os.stat(path)[ST_MODE])[-3:] != PERM:	
				return False
		except OSError as e:
			return False
	if NEWER:
        	try:
            		if os.stat(path).st_mtime <= os.stat(NEWER).st_mtime:
                		return False
		except OSError as e:
				return False
	if UID:
		if os.path.islink(path):
			return True
		try:
			if os.stat(path).st_uid != int(UID):
				return False
		except OSError as e:
			return False
	if GID:
		try:
			if os.stat(path).st_gid != int(GID):
				return False
		except OSError as e:
			if os.path.islink(path):
				if os.lstat(path).st_gid == int(GID):
					return True
	return True

ARG = sys.argv[2:]
COUNT = 0

while COUNT < len(ARG):
	if ARG[COUNT] == '-type':
		COUNT += 1
		TYPE = ARG[COUNT]
	elif ARG[COUNT] == '-executable':
		EXECUTABLE = True
	elif ARG[COUNT] == '-readable':
		READABLE = True
	elif ARG[COUNT] == '-writable':
		WRITABLE = True
	elif ARG[COUNT] == '-empty':
		EMPTY = True
	elif ARG[COUNT] == '-name':
		COUNT += 1
		NAME = ARG[COUNT]
	elif ARG[COUNT] == '-path':
		COUNT += 1
		PATH = ARG[COUNT]
	elif ARG[COUNT] == '-regex':
		COUNT += 1
		REGEX = ARG[COUNT]
	elif ARG[COUNT] == '-perm':
                COUNT += 1
                PERM = ARG[COUNT]
	elif ARG[COUNT] == '-newer':
                COUNT += 1
                NEWER = ARG[COUNT]
	elif ARG[COUNT] == '-uid':
                COUNT += 1
                UID = ARG[COUNT]
	elif ARG[COUNT] == '-gid':
                COUNT += 1
                GID = ARG[COUNT]
	else:
		usage(1)
	COUNT += 1

if TYPE == '' or TYPE == 'd':
	if include(DIRECTORY):
		print DIRECTORY

for root, dirs, files in walk(DIRECTORY):
	if TYPE == 'f':
		for f in files:
			if os.path.isfile(root+'/'+f) and include(root+'/'+f):
					print root+'/'+f
	elif TYPE == 'd':
                for d in dirs:
                        if os.path.isdir(root+'/'+d) and include(root+'/'+d):
				print root+'/'+d
	else:
		for f in files:	
			if include(root+'/'+f):
				print root+'/'+f
		for d in dirs:
			if include(root+'/'+d):
				print root+'/'+d
