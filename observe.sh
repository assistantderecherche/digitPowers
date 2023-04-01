#!/bin/bash

watch -tn 1 'ps aux | grep run.0 | grep -v grep | grep -v S | wc -l'
