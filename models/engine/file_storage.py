#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):

        return FileStorage.__objects