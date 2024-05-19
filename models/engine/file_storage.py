#!/usr/bin/python3
"""file_storage module"""
from models.base_model import BaseModel
import json
import os

class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
         """Sets in __objects the obj with key <obj class name>.id."""
         key = f"{obj.__class__.__name__}.{obj.id}"
         self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        dict_rep = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict_rep, file)

    def reload(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        try:
            with open(self.__file_path, 'r') as f:
                serialized_objs = json.load(f)
                for key, value in serialized_objs.items():
                    class_name = key.split('.')[0]
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        except Exception:
            pass



