#!/bin/bash

function f() {
    sleep "$1"
    echo "$1"
}

while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait

# ./sleepsort.sh 5 3 6 3 6 3 1 4 7
