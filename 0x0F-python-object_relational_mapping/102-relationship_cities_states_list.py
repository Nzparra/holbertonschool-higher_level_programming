#!/usr/bin/python3
""" City """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    sql = session.query(City).order_by(City.id).all()
    for citie in sql:
        print("{}: {} -> {}".
              format(citie.id, citie.name, citie.state.name))
    session.close()
