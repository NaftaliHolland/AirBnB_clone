"""
This module define a BaseModel class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Class That defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        my_uuid = uuid.uuid4()
        self.id = str(my_uuid)

        if len(kwargs) > 0:
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
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
