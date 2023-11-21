#!/usr/bin/python3
"""
base_model module: Defines the BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class: Represents a base model with common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If instantiated with keyword arguments (kwargs),
        it reconstructs the object from a dictionary representation.
        Otherwise, it assigns a unique ID, creation time,
        and update time to the instance and adds it to the storage.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current
        datetime and saves the changes to the storage.

        This method updates the 'updated_at' attribute of the object with the
        current datetime and then triggers the storage to save the changes.
        """
        self.updated_at = datetime.today()
        models.storage.save()
        
    def to_dict(self):
        """
        Converts the BaseModel object to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the object's attributes and metadata,
            suitable for serialization.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        Returns a string representation of the BaseModel object
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
