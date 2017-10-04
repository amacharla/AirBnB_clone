#!/usr/bin/python3
""" Module with `Review` class that inherates from BaseModel """
from models import BaseModel

class Review(BaseModel):
    """ Review subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `Review` class """

        review_attr = {"place_id": "", "user_id": "", "text": ""}

        [setattr(self, key, kwargs.pop(key, value))
                for key, value in review_attr.items()]

        super().__init__(*args, **kwargs)
