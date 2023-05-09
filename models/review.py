#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Review written texts.
    """

    place_id = ""
    user_id = ""
    text = ""
