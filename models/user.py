#!/usr/bin/python3
'''Definition of the class user that inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Definition of the class user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
