#!/usr/bin/python

import sqlite3 as sl
import sys
import settings

if len(sys.argv) == 1:
   exit(0) 

con = sl.connect(settings.DATABASE_PATH)

with con:
    local_max = con.execute('SELECT MAX(tex_id) FROM TASK')
    curr_max = local_max.fetchall()[0][0]
    new_max = 1 if curr_max == None else curr_max + 1


sql = 'INSERT INTO TASK (tex_id, name) values(?, ?)'
data = [
    (new_max, sys.argv[1]),
]

with con:
    con.executemany(sql, data)

f = open(settings.TASK_TEX_FILE, 'w')

with con:
    data = con.execute('SELECT name FROM TASK')
    f.write(r'\begin{enumerate}' + '\n')
    for row in data:
        f.write('\t\item ' + str(row[0]) + '\n')
    f.write('\end{enumerate}')

f.close()
