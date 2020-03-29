#!/usr/bin/python3
"""model state"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state, citie in session.query(State, City)\
            .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, citie.id, citie.name))
    session.commit()
    session.close()
