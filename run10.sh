#!/bin/bash

val=10
logfile=${val}.log

rm $logfile > /dev/null 2>&1 

python3 run10.py >> $logfile 2>&1 &
