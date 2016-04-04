#!/bin/sh

if ! [ -x ./timeout.py ]; then
	echo "Failure - script is not executable"
	echo 1
fi



if [ "$(cat ./timeout.py | head -n 1 | grep python2.7)" == "" ]; then
	echo "Failure - script does not contain python2.7"
fi



echo "timeout.py test successful"

