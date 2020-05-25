# Author      : Trenton Stiles
# Name        : dbTest.py
# Description : a unit test to verify functions inside db.py file
#               work as intended too.

import db
import os
import logger

# logger is just a fancy py file to print out log messages and save
# them to a log file with time stamp.
log = logger.Logger()

# establish database connection. as of right now its as if creating
# production database. must add new init to db to make a mockup one.
db = db.Db()

# checks if the sqlite db file exists. insures the Db init class can
# at least make the database.
def dbExistTest():
    exists = os.path.exists("login_manager.db")
    if(exists):
        log.message("DB Exists", log.SUCCESS)
    else:
        log.message("DB does not exists", log.FAIL)

# checks if admin accounts exists and default password hash matches.
# insures Db.__init__() inserts default admin to DB and we verify.
# Db.compare_hash() can select an account and verify password hashes.
def dbTestAdminAccount():
    result = db.compare_hash("admin", "changeme")
    if(result):
        log.message("Admin hash check good", log.SUCCESS)
    else:
        log.message("Admin hash check bad", log.FAIL)



if __name__ == "__main__":
    tests = [dbExistTest, dbTestAdminAccount]
    for test in tests:
        test()


