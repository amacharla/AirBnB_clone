#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


storage = FileStorage()  # insatance of file storage
storage.reload()  # deserializes JSON file to `__objects()`
