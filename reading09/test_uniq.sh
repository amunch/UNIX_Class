#!/bin/bash

if ! diff -u <(cat /etc/passwd | cut -d : -f 7 | sort | uniq) <( cat /etc/passwd | cut -d : -f 7 | sort | ./uniq.py); then
    echo "uniq test failed!"
    exit 1
fi

if ! diff -u <(cat /etc/passwd | cut -d : -f 7 | sort | uniq -c) <( cat /etc/passwd | cut -d : -f 7 | sort | ./uniq.py -c); then
    echo "uniq -c test failed!"
    exit 1
fi

echo "uniq test successful!"
