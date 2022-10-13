#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "place"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description =  Column(String(128))
    number_rooms =  Column(Integer, nullable=False, defualt=0)
    number_bathrooms = Column(Integer, nullable=False, defualt=0)
    max_guest = Column(Integer, nullable=False, defualt=0)
    price_by_night = Column(Integer, nullable=False, defualt=0)
    latitude = Column(Float)
    longitude =  Column(Float)
    amenity_ids = []
