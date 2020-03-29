#!/usr/bin/python3
import sys
import MySQLdb as sql


if __name__ == "__main__":
    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    sq = db.cursor()
    sq.execute("SELECT cities.id, cities.name, states.name FROM cities \
               JOIN states on cities.state_id = states.id ORDER BY id ASC;")
    for row in sq:
        print("{}".format(row))
    sq.close()
    db.close()
