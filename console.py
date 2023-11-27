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
from models import storage

from models.__init__ import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    global CHILD_CLASSES
    global OBJECTS

    CHILD_CLASSES = [cls.__name__ for cls in BaseModel.__subclasses__()]
    CHILD_CLASSES.append("BaseModel")
    OBJECTS = storage.all()

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
            if line in CHILD_CLASSES:
                class_name = globals()[line]
                new_instance = class_name()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class"""
        
        if line:
            a = line.split(" ")
            if a[0] in CHILD_CLASSES:
                if len(a) > 1:
                    key = f"{a[0]}.{a[1]}"
                    if key in OBJECTS.keys():
                        class_name = globals()[a[0]]
                        new_instance = class_name(**OBJECTS[key])
                        print(new_instance)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ deletes an instance based on the class name and id """
        if line:
            a = line.split(" ")
            if len(a) > 1:
                if a[0] in CHILD_CLASSES:
                    key = f"{a[0]}.{a[1]}"
                    if key in OBJECTS.keys():
                        class_name = globals()[a[0]]
                        new_instance = class_name(**OBJECTS[key])
                        new_instance.destroy()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
