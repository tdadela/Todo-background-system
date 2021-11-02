#!/usr/bin/python
import sqlite3
import settings

con = sqlite3.connect(settings.DATABASE_PATH)

try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE TASK (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tex_id INTEGER NOT NULL,
                name TEXT NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE DONE (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE OLD_TASKS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
    print('Could not complete operation:', e)

con.close()
