#!/bin/bash

watch -tn 1 'ps aux | grep python | grep $USER | grep run.. | grep -v grep | grep -v S | grep -v ipykernel_launcher | wc -l'
