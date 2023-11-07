"""
This module define a BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Class That defines all common attributes/methods for other classes
    """
    def __init__(self):
        my_uuid = uuid.uuid4()
        self.id = str(my_uuid)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}")

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        self.__dict__["class"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
