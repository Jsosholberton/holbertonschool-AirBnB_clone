#!/usr/bin/python3
''''''
import json
from models.base_model import BaseModel


class FileStorage():
    ''''''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''''''
        return FileStorage.__objects

    def new(self, obj):
        ''''''
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        ''''''

    def reload(self):
        ''''''
        return