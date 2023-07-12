#!/usr/bin/python3
'''Definition of the class'''
import json
import cmd


class HBNBCommand(cmd.Cmd):
    """class hbnb console command"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''
        Description:
        ***********
            Command to exit the console
        Args:
        *****
            Line (any): string with the command
        '''
        return True

    def do_EOF(self, line):
        '''
        Description:
        ************
            Command to exit the console by EOF
        Args:
        *****
            line (any): string with the command
        '''

        return True

    def empyline(self):
        '''
        Description:
        ************
            Ignore the blank lines
        '''

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
