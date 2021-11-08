#!/usr/bin/python
'''
Get a list of tasks and finished tasks from the database
and write them into a tex file.
'''
import settings
import db_operation

with open(settings.TASK_TEX_FILE, 'w') as f:
    try:
        data = db_operation.select_all_tasks(settings.DATABASE_PATH, 'TASK')
        if len(data) != 0:
            f.write(r'Todo:\\' + '\n')
            f.write(r'\begin{enumerate}' + '\n')
            for row in data:
                f.write('\t\\item ' + str(row[0]) + '\n')
            f.write('\\end{enumerate}\n')

        data = db_operation.select_all_tasks(settings.DATABASE_PATH, 'DONE')
        if len(data) != 0:
            f.write(r'Done:\\' + '\n')
            f.write(r'\begin{itemize}' + '\n')
            for row in data:
                f.write('\t\\item ' + str(row[0]) + '\n')
            f.write(r'\end{itemize}')

    finally:
        f.close()
