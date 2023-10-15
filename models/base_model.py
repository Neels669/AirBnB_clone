#!/usr/bin/env python3
"""This module is the base class of all our models."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ instantiation """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Print object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """"returns a dictionary containing all keys/values of instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = (self.__class__.__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
