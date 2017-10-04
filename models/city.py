#!/usr/bin/python3
""" Module with City subclasee """
from models import BaseModel


class City(BaseModel):
    """ City subclass """

    def __init__(self, *args, **kwargs):
        """ Init method for `City` class """

        self.state_id = kwargs.pop("State.id", "")
        self.name = kwargs.pop("name", "")
        super().__init__(*args, **kwargs)
