#!/usr/bin/python3
"""Relationship city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
