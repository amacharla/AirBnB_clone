#!/usr/bin/python3
""" Module FileStorage
    that searializes instance to JSON file and
    deserializes JSON file to instances
"""
import json

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
        # value = Instances dict <- JSON str <- converted to <- Objects dict
        self.__objects[key] = obj.to_dict()  # holds multiple instances

    def save(self):
        """ serializes `__objects` to the JSON file """

        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'w') as json_file:
                json.dump(self.__objects, json_file)
        except:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:  # if file doesnt exist dont do anything
            with open(self.__file_path, 'r') as json_file:
                instances = json.load(json_file)
        except:
            pass
        else:  # if exist recreate instance
            for instance, attributes in instances.items():
                self.__objects[instance] = eval(attributes['__class__'])(**attributes)
                                              # ex. value = BaseModel(**kwargs)
