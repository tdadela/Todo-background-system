#!/bin/sh
echo DATABASE_PATH=\'`pwd`/todo.db\'   > settings.py
echo TASK_TEX_FILE=\'`pwd`/latex/task.tex\' >> settings.py
echo DONE_TEX_FILE=\'`pwd`/latex/done.tex\' >> settings.py
echo PROJECT_PATH=\'`${0%/*}`\' >> settings.py
