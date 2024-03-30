#!/bin/bash

logdir=$1
mkdir -p "$logdir"
shift
python3 dreamer.py --logdir "$logdir" "$@" 2>&1 | tee "$logdir/logs.txt"