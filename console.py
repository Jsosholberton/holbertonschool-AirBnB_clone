#!/usr/bin/python3
'''Definition of the class'''
import json
import cmd
import shlex
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """class hbnb console command"""

    prompt = "(hbnb) "
    list_class = ["BaseModel"]

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''Exit command to exit the program\n'''

        return True

    def emptyline(self):
        '''Ignore the blank lines'''

        pass

    def do_create(self, line):
        '''Creates a new instance an save it'''
        if len(line) > 0:
            if line in HBNBCommand.list_class:
                instance_tmp = eval(line + "()")
                instance_tmp.save()
                print("{}".format(instance_tmp.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        '''Prints the string representation of an instance by id'''
        
        code_key = line.split()
        if len(line) > 0:
            dict_objets = models.storage.all()
            key = code_key[0] + "." + code_key[1]
            if key in dict_objets:
                print(dict_objets[key])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
