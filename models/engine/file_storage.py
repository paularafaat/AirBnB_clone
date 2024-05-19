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
        return FileStorage.__objects
    
    def new(self, obj):
         """Sets in __objects the obj with key <obj class name>.id."""
         key = f"{obj.__class__.__name__}.{obj.id}"
         FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        dict_rep = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict_rep, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists)."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    serialized_objs = json.load(f)
                    for key, value in serialized_objs.items():
                        class_name = key.split('.')[0]
                        if class_name in globals():
                            cls = globals()[class_name]
                            FileStorage.__objects[key] = cls(**value)
                except Exception:
                    pass



