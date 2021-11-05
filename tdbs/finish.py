#!/usr/bin/python

import sys
import settings
from db_operation import remove, add_to_done

if len(sys.argv) == 1:
   exit(0) 

try:
   int(sys.argv[1])
except ValueError:
   raise ValueError('Argument is not intiger.')

name = remove(settings.DATABASE_PATH, "TASK", sys.argv[1])

if name == '':
    print("There is no task with this number.")
    exit()

add_to_done(settings.DATABASE_PATH, name)
