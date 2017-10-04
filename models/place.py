#!/usr/bin/python3
""" Module with `Place` class that inherates from BaseModel """
from models import BaseModel


class Place(BaseModel):
    """ Place subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `Place` class """

        place_attr = {"city_id": "", "user_id": "",
                      "name": "", "description": "",
                      "number_bathrooms": 0, "number_rooms": 0,
                      "max_guest": 0, "price_by_night": 0, "latitude": 0.0,
                      "longitude": 0.0, "amenity_ids": []}

        [setattr(self, key, kwargs.pop(key, value))
         for key, value in place_attr.items()]

        super().__init__(*args, **kwargs)
