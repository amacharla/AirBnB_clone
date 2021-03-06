#!/usr/bin/python3
""" Module with __init__ and obj_constructor """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def obj_constructor(cls_name, create=0):
    """ Object Contructor, alternative for eval """

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    if cls_name in classes:
        if create:
            return classes[cls_name]()  # return object
        return  # just checking if class exist

    raise NameError  # so try statement will get triggered

storage = FileStorage()  # insatance of file storage
storage.reload()  # deserializes JSON file to `__objects()`
