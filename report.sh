#!/bin/bash

# collect information from all logs:
cat *.log | grep -e '\.\.\.' > report.txt
cat *.log | grep -e '\-\->' >> report.txt

sort report.txt -k3 -n > report.tmp
mv report.tmp report.txt

cat report.txt
