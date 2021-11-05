#!/usr/bin/python

import sqlite3 as sl
import settings

con = sl.connect(settings.DATABASE_PATH)

with con:
    con.execute('INSERT INTO OLD_TASK SELECT * FROM DONE;')
    con.execute('DELETE FROM DONE;')
