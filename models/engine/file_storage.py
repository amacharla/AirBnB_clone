#!/usr/bin/python3
""" Module FileStorage
    that searializes instance to JSON file and
    deserializes JSON file to instances
"""
import json, copy, models
class FileStorage:
    """
    - Searializes Instance to JSON file
    - Desearializes JSON file to Instance
    """

    __file_path = "file.json"
    __objects = {}  # holds all the instances

    def all(self):
        """ Returns: dict of `__objects` which hold instances"""

        return self.__objects

    def new(self, obj):
        """ add instance to `__objects` dict  """

        key = "{0.__class__.__name__}.{0.id}".format(obj)  # id uniq/instance
        # value = Instances
        self.__objects[key] = obj  # holds multiple instances

    def save(self):
        """ serializes `__objects` to the JSON file """

        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'w') as json_file:
                for key, value in self.__objects.items():
                    # serialize obj by calling `to_dict()`
                    self.__objects[key] = value.to_dict()
                # save dict of instances (`class.id = inst.__dict__`) to file
                json.dump(self.__objects, json_file)
        except:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'r') as json_file:
                # json.load process inner dict then outter dict
                # `__object` <- `class.id: object` memory address
                self.__objects = json.load(json_file, object_hook=self._object_decoder)
        except:  # file doesnt exist
            pass

    @staticmethod
    def _object_decoder(obj_dict):
        """ Turns inner dict into object and doesnt modify outter dict """
        # imported here to prevent cicular import
        from models.base_model import BaseModel
        # if dict is inner dict then convert to object
        if '__class__' in obj_dict and obj_dict['__class__'] == 'BaseModel':
            return BaseModel(**obj_dict)  # returns objects memory address
        return obj_dict  # if outter dict (`class.id`) leave as is
