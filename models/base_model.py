#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from import uuid4
from datetime import datetime
import models
from os import environ
import sqlalchemy import create_engine, Coulmn, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if (storage_engine == "db"):
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instialization of the base model"""
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(kwargs[key], iso))
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        new_dict = self.__dict__.copy()
        new_dict = {}
        new_dict.update({"__class__": self.__class__.__name__})
        for key in list(new_dict):
            if key in ("created_at", "updated_at"):
                new_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                new_dict.pop(key)
            else:
                new_dict.update({key: getattr(self, key)})
        return new_dict

    def delete(self):
        """delete the current instance"""
        k = "{}.{}".format(type(self).__name__, self.id)
        del models.storage.__objects[k]
