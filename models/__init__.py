#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

def obj_constructor(cls_name, create=0):

    classes = {"BaseModel": BaseModel, "User": User }

    if cls_name in classes:
        if create:
            return classes[cls_name]()
        return

    raise NameError

storage = FileStorage()  # insatance of file storage
storage.reload()  # deserializes JSON file to `__objects()`
