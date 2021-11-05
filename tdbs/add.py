#!/usr/bin/python

import sys
import settings
from db_operation import add_to_task

if len(sys.argv) == 1:
   exit(0) 

task_name = ' '.join(sys.argv[1:])

add_to_task(settings.DATABASE_PATH, task_name)
