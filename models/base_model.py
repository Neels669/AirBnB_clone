#!/usr/bin/env python3
"""This module is the base class of all our models."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    self.created_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    self.__class__.__name__ = v
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """Print object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """"returns a dictionary containing all keys/values of instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = (self.__class__.__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
