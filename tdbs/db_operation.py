#!/usr/bin/python
import sqlite3

def not_allowed_table_name(name: str):
    if name not in {"TASK", "DONE", "OLD_TASK"}:
        raise ValueError('Not allowed table name.')

def remove(db_path: str, table_name: str, tex_id: int):
    not_allowed_table_name(table_name)
    con = sqlite3.connect(db_path)
    id = str(tex_id)
    task_name = []
    try:
        with con:
            task = con.execute(f'SELECT name FROM {table_name} WHERE tex_id = ?', id)
            con.execute(f'DELETE FROM {table_name} WHERE tex_id = ?', id)
            con.execute(f'UPDATE {table_name} SET tex_id = tex_id - 1 WHERE tex_id > ?', id)
            task_name = task.fetchall()
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
    con.close()
    return '' if task_name == [] else task_name[0]

def add_to_done(db_path: str, task_name: str):
    print(task_name)
    con = sqlite3.connect(db_path)
    try:
        with con:
            con.execute('INSERT INTO DONE (name) VALUES(?)', task_name)
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
    con.close()
