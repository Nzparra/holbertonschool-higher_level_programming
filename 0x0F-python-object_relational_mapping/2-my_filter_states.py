#!/usr/bin/python3
import sys
import MySQLdb as sql

if __name__ == "__main__":
    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    sq = db.cursor()
    sq.execute("SELECT * FROM states WHERE name='{:s}' ORDER BY id ASC"
               .format(sys.argv[4]))
    for row in sq:
        print("{}".format(row))
    sq.close()
    db.close()
