#!/bin/sh
echo DATABASE_PATH=\'`pwd`/todo.db\'   > settings.py
echo TASK_TEX_FILE=\'`pwd`/latex/task.tex\' >> settings.py

python3 create_database.py
