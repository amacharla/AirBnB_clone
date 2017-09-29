#!/usr/bin/python3
""" Module with BaseModel class """
import copy, uuid
from datetime import datetime

class BaseModel():
    """ Base Class """

    def __init__(self):
        """ Base Initilazation """
        self.id = str(uuid.uuid4())  # random uniq id in str format
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String rep: [<class name>] (<self.id>) <self.__dict__> """
        return "[{0.__class__.__name__}] ({0.id}) {0.__dict__}".format(self)

    def save(self):
        """ updates public instance attribute `updated_at` """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns: a dict with all keys/values of __dict__ of instance """
        json_dict = copy.deepcopy(self.__dict__)  # so og dict cant be modified
        json_dict.update({'__class__': self.__class__.__name__,
                          'updated_at': self.updated_at.isoformat(),
                          'created_at': self.created_at.isoformat()})
        return json_dict
