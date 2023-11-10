#!/usr/bin/python3

"""
This module contains class HBNBCommand(cmd.Cmd)
"""

import json
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quits the interpreter"""
        return True

    def do_quit(self):
        """Quit command to exit the program"""
        sys.exit()

    def emptyline(self):
        """Print nothing when an empty line is the input"""
        pass

    def do_create(self, line):
        arguments = line

        if arguments == "BaseModel":
            new_instance = BaseModel()
            new_instance = new_instance.to_dict()
            print(new_instance)
            
            for key in new_instance:
                if key == "id":
                    print(new_instance["id"])
            
            with open("file.json", "w") as file:
                json.dump(new_instance, file)

        elif len(sys.arg) < 2:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class"""
        
        #arguments = line
        #a, b = arguments.split(" ")
        """
        with open("file.json", "r") as file:
            content = json.load(file)
       
        for key in content:
            if content[key] == b:
                print(content.all())
        """

        all_objects = storage.all()
        print(all_objects)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
