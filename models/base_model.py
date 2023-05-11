#!/usr/bin/python3
import uuid
from datetime import datetime

"""
BaseModel define all comon attributes/methods for other classes
"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        This is the constructor of the BaseModel classe
        @*args: it use when we don't know how much arguments will be passed in argument
        @**kwargs; it use when we znat to passed more arguments
        uuid.uuid4() is a methode to return a uniq id
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        We have to print the information initialized
        for print the name of the class we have to choice:
            1- class_name = self.__class__.name and call format(class_name)
            2-format(type(self).__name__)
        __dict__: It automatically transforms the initialized elements into dictionary elements
        """
        return "[{}] ({}) {}".format(type(self).__name, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        The isoformat is use to print with precision time
        """
        my_dct = self.__dict__.copy()
        my_dct['__class__'] = self.__class__.name__
        my_dct['created_at'] = self.created_at.isoformat()
        my_dct['updated_at'] = self.updated_at.isoformat()
        return my_dct
