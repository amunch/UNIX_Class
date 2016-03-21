#!/bin/bash

FLAGS="-c -l -w"

for path in /etc/hosts /etc/passwd; do
    for flag in $FLAGS; do
	if ! diff -u <(wc $flag $path) <(./wc.py $flag $path); then
	    echo "wc test failed on $flag $path!"
	    exit 1
	fi
    done
done

for flag in $FLAGS; do
    if ! diff -u <(cat /etc/passwd | wc $flag) <(cat /etc/passwd | ./wc.py $flag); then
	echo "wc test failed on $flag implicit stdin!"
	exit 1
    fi
done

for flag in $FLAGS; do
    if ! diff -u <(cat /etc/passwd | wc $flag -) <(cat /etc/passwd | ./wc.py $flag -); then
	echo "wc test failed on $flag explicit stdin!"
	exit 1
    fi
done

echo "wc test successful!"
