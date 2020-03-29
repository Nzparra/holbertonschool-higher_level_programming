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
    state = State(name="Louisiana")
    session.add(state)
    new = session.query(State)\
        .filter_by(name=state.name).first()
    print(new.id)
    session.commit()
    session.close()
