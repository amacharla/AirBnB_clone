#!/usr/bin/python3
""" Module with BaseModel class """
import copy
import uuid
import models
from datetime import datetime


class BaseModel:
    """ Base Class """

    def __init__(self, *args, **kwargs):
        """ Base Initilazation
        Args:
            args: not used often, dont know why its here
            kwargs: dict type argument
        Raises:
            Exception: helps prevent failure if user passes in invalid argument
        """

        self.id = str(uuid.uuid4())  # random uniq id in str format
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, value in kwargs.items():  # update attr with kwargs attr
            if key == "__class__":  # ignore __class__ attr
                continue
            try:  # if user passes in invald value for time, uses current time
                if key == "created_at" or key == "updated_at":  # isoformat
                    setattr(self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
            except Exception:
                pass
        if "id" not in kwargs:  # know that its a new instance
            models.storage.new(self)  # send the new instance to __object dict

    def __str__(self):
        """ String rep: [<class name>] (<id>) <__dict__> """
        return "[{0.__class__.__name__}] ({0.id}) {0.__dict__}".format(self)

    def save(self):
        """ updates public instance attribute `updated_at` """
        self.updated_at = datetime.now()
        models.storage.save()  # save all the instances in scope

    def to_dict(self):
        """ Returns: a dict with all keys/values of __dict__ of instance """
        json_dict = copy.deepcopy(self.__dict__)  # so og dict can't modify
        #  `__class__` later used to recreate instance
        json_dict.update({'__class__': self.__class__.__name__,
                          'updated_at': self.updated_at.isoformat(),
                          'created_at': self.created_at.isoformat()})
        return json_dict  # dict in JSON str format & used save attr
