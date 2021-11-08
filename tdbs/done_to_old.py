#!/usr/bin/python

import sys
import datetime
import settings
from db_operation import migrate_done_to_old, last_migration


def last_migration_today():
    '''Check if last migration was today.'''
    today = str(datetime.datetime.combine(datetime.date.today(),
                                          datetime.time.min))
    migration = last_migration(settings.DATABASE_PATH)
    return today >= migration


if sys.argv[-1] == "force" or not last_migration_today():
    migrate_done_to_old(settings.DATABASE_PATH)
