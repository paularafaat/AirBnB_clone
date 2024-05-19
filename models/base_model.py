#!/usr/bin/python3
"""base_modle module"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """BseModel Class"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        The id attribute is assigned a unique UUID string.
        The created_at and updated_at attributes are
        assigned the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute
        with the current datetime.
        This method should be called every
        time an object is changed.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

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

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
