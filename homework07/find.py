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

PROGRAM_NAME = os.path.basename(sys.argv[0]) #Store the name of the program.

DIRECTORY = sys.argv[1] #Store the directory to be searched (first argument after name)
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

def walk(path): #Try to recursively search the directory, and exit if there is an error.
	try:
		return os.walk(path, topdown = True, followlinks = True)
	except OSError as e:	
		print >>sys.stderr, 'Unable to open file{}:{}'.format(path, e)
		sys.exit(1)

#Functions to determine if executable, readable, and writable.
def is_exe(path):
	return os.path.exists(path) and os.access(path, os.X_OK)

def is_read(path):
	return os.path.exists(path) and os.access(path, os.R_OK)

def is_write(path):
	return os.path.exists(path) and os.access(path, os.W_OK)

#Function to determine if the paths hould be included.
def include(path):
	if EXECUTABLE: #If the file is executable.
		if is_exe(path) == False:
			return False
	if READABLE: #If the file is readable.
		if is_read(path) == False:
			return False
	if WRITABLE: #If the file is writable.
		if is_write(path) == False:
			return False
	if EMPTY: #Tell if the directory is empty.
		if os.path.isdir(path):
			try:
				if len(os.listdir(path)) != 0:
					return False
			except OSError as e:
				return False
		elif os.path.isfile(path) and os.stat(path).st_size != 0:
			return False
		elif os.path.islink(path):
			try:
				if os.stat(path):
					return True
			except OSError as e:
				return False
	if NAME: #Tell if the name matches a string in the basename.
		if not fnmatch.fnmatch(os.path.basename(path), NAME):
			return False
	if PATH: #Match the path to the specified path name.
		if not fnmatch.fnmatch(path, PATH):
			return False
	if REGEX: #Search for this regular expression
		if not re.search(REGEX, path):
			return False
	if PERM: #Permission are exactly the mode specified.
		try:
			if oct(os.stat(path)[ST_MODE])[-3:] != PERM:	
				return False
		except OSError as e:
			return False
	if NEWER: #File was modified more recently than specified file.
        	try:
            		if os.stat(path).st_mtime <= os.stat(NEWER).st_mtime:
                		return False
		except OSError as e:
				return False
	if UID: #Files numeric user ID is as specified.
		try:
			if os.stat(path).st_uid != int(UID):
				return False
		except OSError as e:
			if os.path.islink(path):
				if os.lstat(path).st_uid == int(UID):
					return True
	if GID: #File's group id is as specified.
		try:
			if os.stat(path).st_gid != int(GID):
				return False
		except OSError as e:
			if os.path.islink(path):
				if os.lstat(path).st_gid == int(GID):
					return True
	return True

ARG = sys.argv[2:] #Arguments are the third in the list and on.
COUNT = 0 #Incremented twice with options that need second argument.

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

if TYPE == '' or TYPE == 'd': #Include directory if includable and not of type f.
	if include(DIRECTORY):
		print DIRECTORY

for root, dirs, files in walk(DIRECTORY): #Walk through the directories and include if passes test.
	if TYPE == 'f':
		for f in files:
			if os.path.isfile(root+'/'+f) and include(root+'/'+f):
					print root+'/'+f
	elif TYPE == 'd':
                for d in dirs:
                        if os.path.isdir(root+'/'+d) and include(root+'/'+d):
				print root+'/'+d
	else: #If type is not specified, do both.
		for f in files:	
			if include(root+'/'+f):
				print root+'/'+f
		for d in dirs:
			if include(root+'/'+d):
				print root+'/'+d
