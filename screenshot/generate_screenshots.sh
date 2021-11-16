#!/bin/bash


cd ${0%/*}/
cd ..

mv tdbs/todo.db tdbs/todo.db-
./tdbs/create_database.py

./td add feed cat
./td add take control of the country

rm screenshot/add.png
mv latex/bc-1.png screenshot/add.png

./td finish 1

rm screenshot/finish.png
mv latex/bc-1.png screenshot/finish.png

mv tdbs/todo.db- tdbs/todo.db
