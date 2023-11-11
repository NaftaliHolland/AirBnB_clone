"""
This module holds FileStorage class
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <0bj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
