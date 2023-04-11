#!/bin/bash

low=11
high=20

logfile=${low}-${high}.log

rm $logfile > /dev/null 2>&1 

python3 run.py $low $high >> $logfile 2>&1 &
