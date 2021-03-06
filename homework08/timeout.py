#!/usr/bin/env python2.7
#By: Andy Munch
#Worked with Mark Pruitt

import getopt 
import os
import sys
import signal
import errno

SECONDS = 10
VERBOSE = False
CHILDPID = -1
CHILDSTATUS = -1

PROGRAM_NAME = os.path.basename(sys.argv[0]) #Program name for use in error.

def error(message, exit_code=1): #Error sequence.
	print >>sys.stderr, message
	sys.exit(exit_code)

def usage(exit_code=0): #Usage description.  Used for invalid flags for -h.
	error('''Usage: {} options...

Options:

	-t SECONDS  Timeout duration before killing command (default is 10 seconds)
	-v	    Display verbose debugging output'''
	.format(PROGRAM_NAME), exit_code)


def handler(signum, frame): #Handles the alarm.
	print "Alarm triggered after {} seconds!".format(SECONDS)

def debug(message, *args): #Debugs if verbose is set to true.
	if VERBOSE == True:
		print message.format(*args)

try: #getopts to handle command line arguments.
	opts, args = getopt.getopt(sys.argv[1:], "t:vh")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts: 
	if o == '-t':
		SECONDS = a #Set to command line argument.
	elif o == '-v':
		VERBOSE = True
	else:
		usage(1)

if len(args) == 0: #Need a command to properly execute.
	print "Please specify a command"
	usage(1)

FIRST = args[0]
SPACE = " "
COMMAND = SPACE.join(args)
debug('Executing "{}" for at most {} seconds...', COMMAND, SECONDS)
 
try: #Try to fork the process.
	debug('Forking...')
	pid = os.fork()
	signal.signal(signal.SIGALRM, handler) #Set the alarm.
	if pid == 0: #Child process.
		try:
			debug('Execing...') #Try to execute the command.
			os.execvp(FIRST, args)
		except OSError as e:
			error('Unable to exec: {}', e)
	else:
		try:
			signal.alarm(int(SECONDS)) #Set alarm for 5 seconds.
			debug('Enabling Alarm...')
			debug('Waiting...')
			pid, status = os.wait() #Wait for the child process to finish.
		except OSError as e:
			if e.errno == errno.EINTR: #Run if the alarm interruts the process.
				debug('Killing PID {}...', pid)
				os.kill(pid, signal.SIGHUP) #Kill the child process.
				pid, status = os.wait()
			else:
				error(e)
	signal.alarm(0) #Disable the alarm by setting to 0.
        debug('Disabling Alarm...')
        debug('Process {} terminated with exit status {}', pid, status)
	sys.exit(status)
except OSError as e: #Catch error if not successfully forked.
	error('Unable to fork: {}', e)
