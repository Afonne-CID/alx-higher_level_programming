#!/usr/bin/python3
""" Lists all cities from the `hbtn_0e_4_usa` database
    Usage: ./5-filter_cities.py \
            <mysql username> \
            <mysql password> \
            <mysql db name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                FROM `cities` c \
                JOIN `states` s \
                    ON s.id = c.state_id \
                ORDER BY c.id")

    print(cur.fetchall())

    cur.close()
    db.close()
