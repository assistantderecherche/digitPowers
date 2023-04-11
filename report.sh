#!/bin/bash

cat *.log | grep -e '\.\.\.' > tmp
cat *.log | grep -e '\-\->' >> tmp
sort tmp -k3 -n > report.txt
rm tmp
cat report.txt
