#!/usr/bin/python3
import sys
import MySQLdb as sql


def safe():
    if len(sys.argv) == 5:
        db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
        sq = db.cursor()
        s = sys.argv[4]
        sq.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC;", (s, ))
        for row in sq:
            print("{}".format(row))
        sq.close()
        db.close()
    else:
        print("BUEN INTENTO")
        return


if __name__ == "__main__":
    safe()
