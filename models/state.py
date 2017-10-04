#!/usr/bin/python3
""" Module with State subclasee """
from models import BaseModel


class State(BaseModel):
    """ State subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `User` class """

        self.name = kwargs.pop("name", '')
        super().__init__(*args, **kwargs)
