#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a User.

    Attributes:
        email (str): user email address.
        password (str): the user password to be used to log in.
        first_name (str): user's first name.
        last_name (str): user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
