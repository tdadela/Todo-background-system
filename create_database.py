#!/usr/bin/python
import sqlite3 as sl
import settings

con = sl.connect(settings.DATABASE_PATH)

with con:
    con.execute("""
        CREATE TABLE TASK (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            tex_id INTEGER NOT NULL,
            name TEXT NOT NULL
        );
    """)

with con:
    con.execute("""
        CREATE TABLE DONE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)

with con:
    con.execute("""
        CREATE TABLE OLD_TASKS (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)