#!/usr/bin/python=3
"""This module defines class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""  # It will be the State.id
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
