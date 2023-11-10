"""
This module holds FileStorage class
"""
import json
from models.base_model import BaseModel

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
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        my_dict = {}
        for k, v in FileStorage.__objects.items():
            my_dict[k] = v.to_dict()

 
        with open(FileStorage.__file_path, "w") as file:
            json.dump(my_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        
        try:
            with open(FileStorage.__file_path, "r") as file:
                content = file.read()

            objects = eval(content)
            for (key, value) in objects.items():
                objects[key] = eval(key.split('.')[0] + '(**value)')
            print(type(objects))
            self.__objects = objects


        except FileNotFoundError:
            pass

        """

        def reload(self):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    #my_obj = myFile.read()
                    objects = json.loads(file)

                    for key, value in objects.items():
                        if '.' in key:  # Checking if the dot exists in the key
                            class_name, obj_id = key.split('.')
                            # Assuming your classes are imported properly, create instances dynamically
                            if class_name == 'BaseModel':
                                from models.base_model import BaseModel  # Import the specific class dynamically
                                obj = BaseModel(**value)  # Create an instance of BaseModel
                                objects[key] = obj

                    self.__objects = objects

            except FileNotFoundError:
                pass
