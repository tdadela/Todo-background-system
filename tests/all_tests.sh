#!/bin/bash

cd ${0%/*}

echo "Test 1: " `./test1.sh 2> /dev/null | tail -1`
echo "Test 2: " `./test2.sh 2> /dev/null | tail -1`

