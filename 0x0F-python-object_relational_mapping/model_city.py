#!/usr/bin/python3
"""model state!"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class city!"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
