#!/usr/bin/python
import sqlite3
import settings

con = sqlite3.connect(settings.DATABASE_PATH)

try:
    with con:
        cur = con.cursor()
        cur.executescript("""
            CREATE TABLE TASK (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tex_id INTEGER NOT NULL,
                name TEXT NOT NULL
            );

            CREATE TABLE DONE (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );

            CREATE TABLE OLD_TASK (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );

            CREATE TABLE MIGRATION (
                last_migration timestamp NOT NULL
            );

            CREATE TABLE HABIT (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT DEFAULT "" NOT NULL,
                created timestamp NOT NULL,
                first_day timestamp,
                last_day timestamp
            );

            CREATE TABLE HABIT_STATUS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT DEFAULT "" NOT NULL
            );

            CREATE TABLE HABIT_TRACKING (
                habit_id INTEGER NOT NULL,
                status_id INTEGER NOT NULL,
                day timestamp,

                CONSTRAINT fk_habit
                FOREIGN KEY (habit_id)
                REFERENCES HABIT_TRACKING (_id)

                CONSTRAINT fk_status
                FOREIGN KEY (status_id)
                REFERENCES HABIT_TRACKING (id)
            );
        """)
        cur.execute("""
        INSERT INTO MIGRATION VALUES(CURRENT_TIMESTAMP);
        """)
except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
    print('Could not complete operation:', err)

con.close()
