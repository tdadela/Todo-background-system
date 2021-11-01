#!/usr/bin/python

import sqlite3 as sl
import settings

con = sl.connect(settings.DATABASE_PATH)
f = open(settings.TASK_TEX_FILE, 'w')

with con:
    data = con.execute('SELECT name FROM TASK')
    if data != []:
        f.write(r'Todo:\\' + '\n')
        f.write(r'\begin{enumerate}' + '\n')
        for row in data:
            f.write('\t\item ' + str(row[0]) + '\n')
        f.write('\end{enumerate}')

    data = con.execute('SELECT name FROM DONE')
    if data != []:
        f.write(r'Done:\\' + '\n')
        f.write(r'\begin{itemize}' + '\n')
        for row in data:
            f.write('\t\item ' + str(row[0]) + '\n')
        f.write('\end{itemize}')

f.close()
