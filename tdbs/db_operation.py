#!/usr/bin/python
import sqlite3


def not_allowed_table_name(name: str):
    '''Check if given string is allowed table name.'''
    if name not in {"TASK", "DONE", "OLD_TASK"}:
        raise ValueError('Not allowed table name.')


def remove(db_path: str, table_name: str, tex_id: str):
    '''Remove task with given tex_id and return its name.'''
    not_allowed_table_name(table_name)
    con = sqlite3.connect(db_path)
    task_name = []
    try:
        with con:
            task = con.execute(
                f'SELECT name FROM {table_name} WHERE tex_id = ?', (tex_id,))
            con.execute(
                f'DELETE FROM {table_name} WHERE tex_id = ?', (tex_id,))
            con.execute(
                f'''UPDATE {table_name} SET
                tex_id = tex_id - 1 WHERE tex_id > ?''', (tex_id,))
            task_name = task.fetchall()
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
        print('Could not complete operation:', err)
    con.close()
    return '' if len(task_name) == 0 else task_name[0]


def remove_using_id(db_path: str, table_name: str, id: str):
    '''Remove task with given id and return its name.'''
    not_allowed_table_name(table_name)
    con = sqlite3.connect(db_path)
    task_name = []
    try:
        with con:
            task = con.execute(
                f'SELECT name FROM {table_name} WHERE id = ?', (id,))
            con.execute(
                f'DELETE FROM {table_name} WHERE id = ?', (id,))
            con.execute(
                f'''UPDATE {table_name} SET
                tex_id = tex_id - 1 WHERE id > ?''', (id,))
            task_name = task.fetchall()
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
        print('Could not complete operation:', err)
    con.close()
    return '' if len(task_name) == 0 else task_name[0]


def select_all_tasks(db_path: str, table_name: str):
    '''Select and return all task names from a given table.'''
    not_allowed_table_name(table_name)
    con = sqlite3.connect(db_path)
    task_list = []
    try:
        with con:
            tasks = con.execute(
                f'SELECT name, id FROM {table_name} ORDER BY id')
            task_list = tasks.fetchall()
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
        print('Could not complete operation:', err)
    finally:
        con.close()
    return task_list


def add_to_task(db_path: str, task_name: str):
    '''Add new task to TASK table.'''
    con = sqlite3.connect(db_path)
    try:
        with con:
            local_max = con.execute('SELECT MAX(tex_id) FROM TASK')
            curr_max = local_max.fetchall()[0][0]
            new_max = 1 if curr_max is None else curr_max + 1
            con.execute(
                'INSERT INTO TASK (tex_id, name) values(?, ?)',
                (new_max, task_name))
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
    con.close()


def add_to_done(db_path: str, task_name: str):
    con = sqlite3.connect(db_path)
    try:
        with con:
            con.execute('INSERT INTO DONE (name) VALUES(?)', task_name)
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
    con.close()


def migrate_done_to_old(db_path: str):
    con = sqlite3.connect(db_path)
    try:
        with con:
            con.execute('INSERT INTO OLD_TASK SELECT * FROM DONE;')
            con.execute('DELETE FROM DONE;')
            con.execute('''UPDATE MIGRATION SET last_migration
            = CURRENT_TIMESTAMP''')
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
    con.close()


def last_migration(db_path: str):
    ''' Return value of last tasks migration. '''
    con = sqlite3.connect(db_path)

    try:
        with con:
            migration = con.execute(
                'SELECT last_migration FROM MIGRATION;').fetchall()[0][0]
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
        print('Could not complete operation:', e)
        return None
    finally:
        con.close()
    return migration
