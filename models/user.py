#!/usr/bin/python3
""" Module with `user` class that inherates from BaseModel """
from models import BaseModel

class User(BaseModel):
    """ User subclass """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


