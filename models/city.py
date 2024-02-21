#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
import models.state import State
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ representation of city """
    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
