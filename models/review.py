""" Contains review class """
from .base_model import BaseModel


class Review(BaseModel):
    """ Defines Review class """

    place_id = ""
    user_id = ""
    text = ""
