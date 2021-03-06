#!/bin/bash


cd ${0%/*}/
dir_test=`pwd`
cd ..

mv tdbs/todo.db tdbs/todo.db-
./tdbs/create_database.py

./td add t1
./td add t2
./td add t3
./td refresh
./td finish 2
./td migrate
./td done 1
./td add t4
./td add t5
./td remove 3

rm tests/img/test1.png
mv latex/bc-1.png tests/img/test1.png
mv tdbs/todo.db- tdbs/todo.db

cd "$dir_test"
idiff ./img/test1.png ./img/expected1.png
