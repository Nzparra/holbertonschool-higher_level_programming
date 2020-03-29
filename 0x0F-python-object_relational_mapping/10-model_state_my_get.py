#!/usr/bin/python3
"""model state"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = []
    for aid in session.query(State.id)\
            .filter(State.name == '{:s}'.format(argv[4])):
        state.append(aid)
    try:
        print(state[0][0])
    except:
        print("Not found")
    session.close()
