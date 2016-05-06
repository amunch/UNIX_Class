#!/bin/sh
#Timeout shell test script.
#By: Andy Munch

if ! [ -x ./timeout.py ]; then
	echo "Failure - script is not executable"
	exit 1
fi



if [ "$(cat ./timeout.py | head -n 1 | grep python2.7)" == "" ]; then
	echo "Failure - script does not contain python2.7"
	exit 1
fi

if [ "$(./timeout.py -h 2>&1 | grep Usage)" == "" ]; then
	echo "Failure - script does not contain error message"
	exit 1
fi

NUMS=$(seq 1 4)

for num in $NUMS; do
	if [ "$(./timeout.py -t 5 sleep $num && echo Success | grep Success)" == "" ]; then
		echo "Failure on sleep execution in checking for Success"
		exit 1
	fi 
done 

NUMS=$(seq 2 5)

for num in $NUMS; do
	if [ "$(./timeout.py -t 1 sleep $num || echo Failure | grep Success)" == "" ]; then
                echo "Failure on sleep execution in checking for Failure"
                exit 1
        fi
done

if [ "$(./timeout.py -v sleep 1 2>&1 | grep Forking)" == "" ]; then
        echo "Failure - script does not contain debugging messages"
        exit 1
fi


echo "timeout.py test successful"
exit 0
