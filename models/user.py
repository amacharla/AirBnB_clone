#!/usr/bin/python3
""" Module with `user` class that inherates from BaseModel """
from models import BaseModel

class User(BaseModel):
    """ User subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `User` class """

        usr_attr = ["email", "password", "first_name", "last_name"]
        attr_dict = {}
        for key, value in kwargs.items():
            if key in usr_attr:
                setattr(self, key, value)
            else:  # send all other attr to parent classes __init__ method
                attr_dict[key] = value

        super().__init__(*args, **attr_dict)
