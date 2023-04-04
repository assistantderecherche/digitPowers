#!/bin/bash

val=20
logfile=${val}.log

rm $logfile > /dev/null 2>&1 

python3 run20.py >> $logfile 2>&1 &
