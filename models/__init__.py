#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()  # insatance of file storage
storage.reload()  # deserializes JSON file to `__objects()`
