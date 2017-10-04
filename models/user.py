#!/usr/bin/python3
""" Module with `user` class that inherates from BaseModel """
from models import BaseModel

class User(BaseModel):
    """ User subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `User` class """

        usr_attr = ["email", "password", "first_name", "last_name"]
        [setattr(self, key, kwargs.pop(key, ""))
                for key in usr_attr]

        super().__init__(*args, **kwargs)
