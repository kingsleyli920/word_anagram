#! /bin/bash
if [ ! $1 ]; then
    python3 ./solution.py
else
    $1 ./solution.py $2
fi
