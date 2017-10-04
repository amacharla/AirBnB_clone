#!/usr/bin/python3
""" Module FileStorage
    that searializes instance to JSON file and
    deserializes JSON file to instances
"""
import json
import copy
import models  # remove models


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

        json_dict = {}
        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'w') as json_file:
                for key, obj in self.__objects.items():
                    # serialize obj by calling `to_dict()`
                    json_dict[key] = obj.to_dict()
                # save dict of instances (`class.id = inst.__dict__`) to file
                json.dump(json_dict, json_file)
        except FileNotFoundError:
            del json_dict
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'r') as json_file:
                # json.load process inner dict then outter dict
                # `__object` <- `class.id: object` memory address
                self.__objects = json.load(json_file,
                                           object_hook=self.object_decoder)
        except:  # file doesnt exist
            pass

    @staticmethod
    def object_decoder(obj_dict):
        """ Turns inner dict into object and doesnt modify outter dict """
        # imported here to prevent cicular import
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        # if dict is inner dict then convert to object
        if '__class__' in obj_dict:  # returns objects memory address
            if obj_dict['__class__'] == "BaseModel":
                return BaseModel(**obj_dict)
            if obj_dict['__class__'] == "User":
                return User(**obj_dict)
            if obj_dict['__class__'] == "State":
                return State(**obj_dict)
            if obj_dict['__class__'] == "City":
                return City(**obj_dict)
            if obj_dict['__class__'] == "Amenity":
                return Amenity(**obj_dict)
            if obj_dict['__class__'] == "Place":
                return Place(**obj_dict)
            if obj_dict['__class__'] == "Review":
                return Review(**obj_dict)
        else:
            return obj_dict  # if outter dict (`class.id`) leave as is
