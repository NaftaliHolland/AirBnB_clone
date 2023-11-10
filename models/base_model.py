"""
This module define a BaseModel class.
"""
import uuid
from datetime import datetime
#from models.__init__ import storage
import models

class BaseModel:
    """
    Class That defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        my_uuid = uuid.uuid4()
        self.id = str(my_uuid)
        models.storage.new(self)
        
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    kwargs[key] = (
                                datetime.fromisoformat(kwargs[key])
                                if key in ("created_at", "updated_at")
                                else kwargs[key])
                    setattr(self, key, kwargs[key])
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}]"
                f"({self.id}) {str(self.__dict__)}")

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
