#!/bin/sh
echo DATABASE_PATH=\'`pwd`/todo.db\'   > settings.py
echo TASK_TEX_FILE=\'`pwd`/task.tex\' >> settings.py
echo DONE_TEX_FILE=\'`pwd`/done.tex\' >> settings.py
echo PROJECT_PATH=\'`${0%/*}`\' >> settings.py
