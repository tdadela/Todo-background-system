#!/usr/bin/python
'''Finish task with given tex_id.'''
import sys
import settings
from db_operation import remove, add_to_done

if len(sys.argv) == 1:
    sys.exit()

try:
    int(sys.argv[1])
except ValueError:
    print('Argument is not integer.')
    sys.exit()

for t in sys.argv[1:]:
    if t.isdigit():
        name = remove(settings.DATABASE_PATH, "TASK", sys.argv[1])
        if name == '':
            print(f"There is no task with {t} number.")
        elif sys.argv[-1] != "remove":
            add_to_done(settings.DATABASE_PATH, name)
