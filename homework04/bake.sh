#!/bin/sh
#Compiles all of the source files in the directory.
#Homework04 Activity01
#By: Andy Munch
#Collaborated with Mark Pruitt
	
CC=${CC:-gcc}
CFLAGS=${CFLAGS:--std=gnu99 -Wall}
VERBOSE=${VERBOSE:0}
SUFFIXES=${SUFFIXES:-.c}
 
for arg in *$SUFFIXES; do
	name=$(basename "$arg" $SUFFIXES)                
        $CC $CFLAGS -o $name $arg
        if [ $VERBOSE ]; then
        	echo $CC $CFLAGS -o $name $arg
        fi      
   	if [ ! -e $name ]; then
		echo "Failed to compile successfully!"
		exit 1
	fi
done
