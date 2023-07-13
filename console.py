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
        if len(line) > 0:
            code_key = line.split()
            if code_key[0] in HBNBCommand.list_class:
                if len(code_key) == 2:
                    key = code_key[0] + "." + code_key[1]
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        if len(line) > 0:
            code_key = line.split()
            if code_key[0] in HBNBCommand.list_class:
                if len(code_key) == 2:
                    key = code_key[0] + "." + code_key[1]
                    if key in models.storage.all():
                        del models.storage.all()[key]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        "Prints all string representation of all instances"
        if line in HBNBCommand.list_class:
            for key, value in models.storage.all().items():
                if value.to_dict()["__class__"] == line:
                    print(models.storage.all()[key])
        elif not line:
            for show_object in models.storage.all():
                    print(models.storage.all()[show_object])
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
