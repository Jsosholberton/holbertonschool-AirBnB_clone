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
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''''''
        try:
            with open(self.__file_path, mode="r", encoding='utf-8') as file:
                self.__objects = json.loads(file.read())
        except Exception:
            pass
