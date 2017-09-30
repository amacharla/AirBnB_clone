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
    __objects = {}

    def all(self):
        """ Returns: dict of `__objects` """

        return __objects

    def new(self, obj):
        """ set in `__objects` to the JSON file """

        key = "{0.__class__.__name__}.{0.id}".format(obj)
        self.__objects[key] = obj.to_dict()  # get dict rep of obj
        # key changes if different instance thus __objects can hold multiple instances

    def save(self):
        """ serializes `__objects` to the JSON file """

        try:  # if file doesnt exist
            with open(__file_path, 'w') as json_file:
                json.dump(self.__objects, json_file)
        except:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:
            with open(__file_path, 'r') as json_file:
                instances = json.load(json_file)
        except:
            pass
        for instance, attributes in instances.items():
            eval(instance(**attributes))
