#!/usr/bin/env python2.7
#rorschach.py
#By: Andy Munch
#Worked with Mark Pruitt

import getopt
import os
import sys
import yaml
import time
import re
import fnmatch
import stat
 
#Global variables
 
RULES= ".rorschach.yml"
SECONDS= 2
DIRECTORIES= "."
VERBOSE= False
PROGRAM_NAME = os.path.basename(sys.argv[0])
 
#Functions
 
def error(message, *args): 
	print >>sys.stderr, message.format(*args)
	sys.exit(1)
 
def usage(exit_code=0):
	error('''Usage: {} options...
 
	Options:
		-r RULES    Path to rules file (default is .rorschach.yml)
		-t SECONDS  Time between scans (default is 2 seconds)
		-v          Display verbose debugging output
		-h          Show this help message'''.format(PROGRAM_NAME),exit_code)
 
def walk_fd(path):
	try:	
		return os.walk(path, True, None,True)
	except OSError as e:
		print >>sys.stderr, 'Could not open file {}: {}'.format(path, e)
		sys.exit(1)
 
def re_match(name, pattern):
	try:
		return re.match(pattern, name)
	except re.error:
		return False
 
def build_mod(MODTIMES):
	for d in DIRECTORIES:
		for root, dirs, files in walk_fd(d):
			for f in files:
				try:
					MODTIMES[f] = os.path.getmtime(root+"/"+f)
				except OSError as e:
					MODTIMES[f] = 0
 
def debug(message, *args):
	if VERBOSE == True:
		print message.format(*args)
 
try:
	opts,args = getopt.getopt(sys.argv[1:], "t:r:vh")
except getopt.GetoptError as e:
	print e
	usage(1)

NUM = 1
for o, a in opts:
	if o == '-t':
		SECONDS = a
		NUM = NUM + 2
	elif o == '-r':
		RULES = a
		NUM = NUM + 2
	elif o == '-v':
		VERBOSE=True
		NUM = NUM + 1
	else:	
		usage(1)
 
if len(args) != 0:
	DIRECTORIES = sys.argv[NUM:]
 
INFILE = file(RULES, 'r')
debug('Loading yaml file')
RULES = yaml.load(INFILE)

MODTIMES = {}

build_mod(MODTIMES)
 
while 1:
	try:
		for d in DIRECTORIES:
			debug('Checking directory: {}', d)
			for root, dirs, files in walk_fd(d):
				for f in files:
					for rule in RULES:
						if re_match(f,rule['pattern']) or fnmatch.fnmatch(f,rule['pattern']):
							if f not in MODTIMES or MODTIMES[f] != os.path.getmtime(root+"/"+f):
								MODTIMES[f] = os.path.getmtime(root+"/"+f)
								try:
									debug('Forking')
									pid = os.fork()
									if pid ==0: 
 										try:
											action = rule['action'].split(" ")[0]
											try:
												realPath=os.path.abspath(f)
											except OSError as e:
												realPath=root+"/"+f
											obj = rule['action'].format(name=f,path=realPath)
											strobj = obj.split(" ")[0:]
											debug('Executed action {} for {}', action, f)
											os.execvp(action,strobj)
										except OSError as e:
											error('Unable to exec: {}', e)
									else:
										try:
											debug('Waiting')
											pid, status = os.wait()
										except OSError as e:
											error(e)
								except OSError as e:
									error('Unable to fork: {}', e)	
		time.sleep(int(SECONDS))
	except KeyboardInterrupt:	
		sys.exit(1)
