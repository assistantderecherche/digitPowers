#!/bin/bash

low=51
high=55

logfile=${low}-${high}.log

rm $logfile > /dev/null 2>&1 

python3 run.py $low $high >> $logfile 2>&1 &
