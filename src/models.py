import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'people'
    name = Column(String(250), nullable=False)
    gender = Column(String(10), nullable=False)
    hair_color = Column(String(20), nullable=False)
    eye_color = Column(String(30), nullable=False)
    skin_color = Column(String(20), nullable=False)
    url = Column(String(2000), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    url = Column(String(2000), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
  


class Favorite(Base):
    __tablename__ ='favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    people_id = Column(Integer, ForeignKey("people.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    


class User(Base):


    __tablename__ ='user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

