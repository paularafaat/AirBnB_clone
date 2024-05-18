#!/usr/bin/python3
"""base_modle module"""
import uuid
from datetime import datetime


class BaseModel:
    """BseModel Class"""
    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        The id attribute is assigned a unique UUID string.
        The created_at and updated_at attributes are
        assigned the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the updated_at attribute
        with the current datetime.
        This method should be called every
        time an object is changed.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
          __dict__ of the instance.
        A key __class__ is added to this dictionary with
          the class name of the object.
        created_at and updated_at are converted to
        string objects in ISO format.
        """
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
