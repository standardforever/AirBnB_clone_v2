#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = (String(60), Foreignkey(states.id), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
