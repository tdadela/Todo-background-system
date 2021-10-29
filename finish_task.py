#!/usr/bin/python

import sqlite3 as sl
import sys
import settings

if len(sys.argv) == 1:
   exit(0) 

try:
   int(sys.argv[1])
except ValueError:
   raise ValueError('Argument is not intiger.')

con = sl.connect(settings.DATABASE_PATH)

with con:
    task = con.execute('SELECT name FROM TASK WHERE tex_id = ' + sys.argv[1])
    con.execute('DELETE FROM TASK WHERE tex_id = ' + sys.argv[1])
    con.execute('UPDATE TASK SET tex_id = tex_id - 1 WHERE tex_id > ' + sys.argv[1])
    name = task.fetchall()[0]


sql = 'INSERT INTO DONE (name) values(?)'
data = [
    (name),
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

f = open(settings.DONE_TEX_FILE, 'w')

with con:
    data = con.execute('SELECT name FROM DONE')
    f.write(r'\begin{itemize}' + '\n')
    for row in data:
        f.write('\t\item ' + str(row[0]) + '\n')
    f.write('\end{itemize}')

f.close()
