#!/usr/bin/python3
""" States"""

import sys
import MySQLdb as sql

if __name__ == "__main__":
    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    sq = db.cursor()
    sq.execute("SELECT * FROM states WHERE name COLLATE latin1_general_cs\
               LIKE 'N%' ORDER BY id ASC")
    sqq = sq.fetchall()
    for row in sqq:
        print("{}".format(row))
    sq.close()
    db.close()
