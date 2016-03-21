#!/bin/bash

for path in /etc/hosts /etc/passwd; do
    if ! diff -u <(head $path) <(./head.py $path); then
	echo "head test failed on $path!"
	exit 1
    fi
done

if ! diff -u <(cat /etc/passwd | head) <(cat /etc/passwd | ./head.py); then
    echo "head test failed on implicit stdin!"
    exit 1
fi

if ! diff -u <(cat /etc/passwd | head -) <(cat /etc/passwd | ./head.py -); then
    echo "head test failed on explicit!"
    exit 1
fi

for i in $(seq 10); do
    if ! diff -u <(cat /etc/passwd | head -n $i) <(cat /etc/passwd | ./head.py -n $i); then
	echo "head test failed on -n $i!"
	exit 1
    fi
done

echo "head test successful!"
