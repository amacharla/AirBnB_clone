#!/usr/bin/python3
"""
Entry point of the command interpreter
AirBnB Version 1
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command Line Class"""

    prompt = "(hbhb) "

    def do_quit(self, line):
        """quit command"""
        quit()

    def do_EOF(self, line):
        """exit"""
        return (True)

    def emptyline(self):
        """enter empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
