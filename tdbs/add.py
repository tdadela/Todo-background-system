#!/usr/bin/python
'''Add task with given name.'''
import sys
import settings
from db_operation import add_to_task

if len(sys.argv) == 1:
    sys.exit(0)

task_names = ' '.join(sys.argv[1:]).split('.')

for task in task_names:
    if task.strip():
        add_to_task(settings.DATABASE_PATH, task.strip())
