""" This module has the user class """
from .base_model import BaseModel


class User(BaseModel):
    """ A user class that defines the attributes of a user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
