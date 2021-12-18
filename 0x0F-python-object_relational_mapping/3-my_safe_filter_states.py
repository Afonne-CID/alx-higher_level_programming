#!/usr/bin/python3
""" Takes in an argument and displays all values in the `states` table \
            of hbtn_0e_0_usa where name matches the argument \
            (safe from MySQL injections).

   Usage: ./3-my_safe_filter_states.py\
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
