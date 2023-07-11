#!/usr/bin/python3
'''
Description:
************
    Definition of the BaseModel that defines all
    common attributes/methods for other classes

Import:
*******
    uuid (module): (universally unique identifiers) according to RFC 4122.
        uuid4 (function): generate a ramdom UUID number

    datetime (module): Concrete date/time and related types.
        datetime (class): datetime(year, month, day)
            now (method): Construct a datetime from time.time()
            isoformat (method): Return the time formatted according to ISO.

Public instances attributes:
****************************
    id (str): Is a identification of the process
    created_at (datetime): Is the date time of the creation of any element
    updated_at (datetime): Is the date time of the update of any element

Public instances methods:
*************************
    save (method): update the datetime if you use this method
    to_dict (method): return an dictionary with all the attributes from object
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

    def __init__(self, *args, **kwargs):
        '''
        Description:
        ************
            Definition of the method init for his public attributes
        Args:
        *****
            args (list): list of arguments (unused)
            kwargs (dict): dictionary to set his attributes
        '''
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
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
            Made a description of the principal attributes of the object
        Return:
        *******
            A string with the principal attributes of the object
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
