#!/bin/bash

cd ${0%/*}/
dir_test=`pwd`
cd ..

mv tdbs/todo.db tdbs/todo.db-
./tdbs/create_database.py

./run_gui.sh &
flask_pid=$!

./td add t1
./td add t2
./td add t3
./td refresh
wget 127.0.0.1:5000/finish/2
./td migrate
wget 127.0.0.1:5000/finish/1
./td add t4
./td add t5
wget 127.0.0.1:5000/delete/5
./td refresh

kill $flask_pid

mv latex/bc-1.png tests/img/test2.png
mv tdbs/todo.db- tdbs/todo.db

cd "$dir_test"
idiff ./img/test2.png ./img/expected2.png
