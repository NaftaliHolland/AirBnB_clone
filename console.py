#!/usr/bin/python3

"""
This module contains class HBNBCommand(cmd.Cmd)
"""

import json
import cmd
import sys
from models.base_model import BaseModel

from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

from models.__init__ import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    global child_classes
    global objects

    file = FileStorage()
    child_classes = [cls.__name__ for cls in BaseModel.__subclasses__()]
    child_classes.append("BaseModel")
    print(child_classes)

    def do_EOF(self, line):
        """Quits the interpreter"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Print nothing when an empty line is the input"""
        pass

    def do_create(self, line):
        if line:
            if line in child_classes:
                class_name = globals()[line]
                new_instance = class_name()
                new_instance.save()
            else:
                print("** class name doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class"""
        
        if line:
            a = line.split(" ")
            if a[0] in child_classes:
                key = f"{a[0]}.{a[1]}"
                print(objects)
                if key in objects.keys():
                    print(objects[key])
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
