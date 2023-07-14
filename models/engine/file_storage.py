#!/usr/bin/python3
''''''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



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
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w') as file:
            json.dump(dic, file)

    def reload(self):
        ''''''
        try:
            with open(FileStorage.__file_path, mode="r", encoding='utf-8') as file:
                dic = json.load(file)
                for key, value in dic.items():
                    tmp = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = tmp
        except Exception:
            pass
