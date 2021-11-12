#!/bin/sh
# create settings.py
echo DATABASE_PATH=\'`pwd`/tdbs/todo.db\'   > tdbs/settings.py
echo TASK_TEX_FILE=\'`pwd`/latex/task.tex\' >> tdbs/settings.py

# create settings.py for website
echo DATABASE_PATH=\'`pwd`/tdbs/todo.db\'   > app/main/settings.py
echo LIBRARY_PATH=\'`pwd`/tdbs/\'           >> app/main/settings.py

# create database
python3 tdbs/create_database.py
