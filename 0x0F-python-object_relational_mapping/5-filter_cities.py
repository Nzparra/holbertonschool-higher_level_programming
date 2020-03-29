#!/usr/bin/python3
import sys
import MySQLdb as sql


if __name__ == "__main__":
    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    sq = db.cursor()
    sq.execute("SELECT cities.name, states.name FROM cities \
               JOIN states on cities.state_id = states.id \
               WHERE states.name=%s;", (sys.argv[4],))
    st = []
    for row in sq:
        st.append(row[0])
    print(", ".join(st))
    sq.close()
    db.close()
