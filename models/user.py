#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class that will give user info"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
