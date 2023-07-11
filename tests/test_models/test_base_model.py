#!/usr/bin/python3
'''Definition of the test for BaseModel'''
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    '''
    Description:
    ************
        Test for the class BaseModel
    '''

    def test_BaseModel_(self):
        '''
        Description:
        ------------
            Test for id and his variables
        '''

        my_base = BaseModel()
        my_base2 = BaseModel()
        self.assertNotEqual(my_base.id, my_base2.id)
        self.assertTrue(my_base)
        self.assertTrue(type(my_base.id) == str)
        self.assertTrue(type(my_base.created_at) == datetime)
        self.assertTrue(type(my_base.updated_at) == datetime)
        my_base_dict = my_base.to_dict()
        my_base2_dict = my_base2.to_dict()
        self.assertTrue(type(my_base_dict == dict))
        self.assertNotEqual(my_base_dict, my_base2_dict)
