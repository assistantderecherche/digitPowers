#!/bin/bash

cat *.log | grep -e '\.\.\.' > tmp
cat *.log | grep -e '\-\->' >> tmp
sort tmp -k3 -n > REPORT.txt
cat REPORT.txt
