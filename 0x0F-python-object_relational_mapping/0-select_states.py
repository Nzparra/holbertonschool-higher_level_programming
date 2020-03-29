#!/usr/bin/python3
import sys
import MySQLdb as sql

if __name__ == "__main__":
    db = sql.connect(host='localhost', user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    sq = db.cursor()
    sq.execute("SELECT * FROM states ORDER BY id ASC")
    for row in sq:
        print("{}".format(row))
    sq.close()
    db.close()
