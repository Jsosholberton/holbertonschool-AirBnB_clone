#!/usr/bin/python3
'''Definition of the class'''
import json
import cmd


class HBNBCommand(cmd.Cmd):
    """class hbnb console command"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''Exit command to exit the program\n'''

        return True

    def emptyline(self):
        '''
        Description:
        ************
            Ignore the blank lines
        '''

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
