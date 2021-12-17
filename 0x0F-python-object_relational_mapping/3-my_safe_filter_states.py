#!/usr/bin/python3
"""Lists all `states` with a `name` starting with\
            'N'(Case sensitive) from `hbtn_0e_0_usa`
   Usage: ./0-select_states.py\
            <mysql username>\
            <mysql password>\
            <mysql db name>

"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")

    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]

    cur.close()
    db.close()
