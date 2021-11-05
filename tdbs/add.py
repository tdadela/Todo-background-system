#!/usr/bin/python

import sqlite3 as sl
import sys
import settings

if len(sys.argv) == 1:
   exit(0) 

task_name = ' '.join(sys.argv[1:])

con = sl.connect(settings.DATABASE_PATH)

with con:
    local_max = con.execute('SELECT MAX(tex_id) FROM TASK')
    curr_max = local_max.fetchall()[0][0]
    new_max = 1 if curr_max == None else curr_max + 1


sql = 'INSERT INTO TASK (tex_id, name) values(?, ?)'
data = [
    (new_max, task_name),
]

with con:
    con.executemany(sql, data)

