#!/bin/bash

cd ${0%/*}/
cd ..

mv tdbs/todo.db tdbs/todo.db-
./tdbs/create_database.py

./td add t1
./td add t2
./td add t3
./td refresh
./td finish 2
./td migrate
./td finish 1
./td add t4

mv latex/bc-1.png tests/img/test1.png
mv tdbs/todo.db- tdbs/todo.db

cd ${0%/*}/
idiff ./img/test1.png ./img/expected1.png
