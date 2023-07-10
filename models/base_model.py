#!/usr/bin/python3
'''
Description:
************
    Definition of the BaseModel
Import:
*******
    uuid (module): (universally unique identifiers) according to RFC 4122.
        uuid4 (function): generate a ramdom UUID number

    datetime (module): Concrete date/time and related types.
        datetime (class): datetime(year, month, day)
            now (method): Construct a datetime from time.time()
            isoformat (method): Return the time formatted according to ISO.
'''
import uuid
from datetime import datetime


class BaseModel():
    '''
    Description:
    ************
        Definition of the Base Model:
            Defines all common attributes/methods for other classes
    '''
    def __init__(self):
        '''
        Description:
        ************
            Definition of the class init for his public values
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''
        Description:
        ************
            Change the date time when any is update
        '''

        self.update_at = datetime.now()

    def __str__(self):
        '''
        Description:
        ************
            Made a description of the principal elements of the object
        Return:
        *******
            A string with the principal elements of the object
        '''

        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def to_dict(self):
        '''
        Description:
        ************
            Create an dictionary with all the values of the object
        Return:
        *******
            Dictionaty of the object but adding a class name
        '''

        dict_base = self.__dict__
        dict_base["__class__"] = type(self).__name__
        dict_base["created_at"] = dict_base["created_at"].isoformat()
        dict_base["updated_at"] = dict_base["updated_at"].isoformat()

        return dict_base
