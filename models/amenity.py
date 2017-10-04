#!/usr/bin/python3
""" Module with State subclasee """
from models import BaseModel


class Amenity(BaseModel):
    """ Amenity subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `Amenity` class """

        self.name = kwargs.pop("name", '')
        super().__init__(*args, **kwargs)
