#!/usr/bin/python3
"""
Entry point of the command interpreter
AirBnB Version 1
"""
import cmd
from models import storage
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """ Command Line Class """

    intro = "=====Holberton AirBnB Console 0.0.1====="
    prompt = "(hbhb) "
    __instances = storage.all()

    def do_quit(self, line):
        """ Exits the HBNB Console """
        quit()

    def do_EOF(self, line):
        """ If a command handler returns a true value, the program will exit cleanly. """
        return (True)

    def emptyline(self):
        """ Ignores empty line """
        pass

    # Main Functions

    def do_create(self, cls_name):
        """
        Creates a new instance of `BaseModel`

        Usage: create [class name]

        """
        if not cls_name:
            print("** class name missing **")
        else:
            try:  # test if class exist
                instance = eval(cls_name)()
            except NameError:
                print("** class doesn't exist **")
            else:
                print(instance.id)
        return

    def complete_create(self, text, line, begidx, endidx):

        instances = list(self.__instances.keys())
        cls_names = list(set((name.split('.')[0] for name in instances)))
        if not text:
            completions = cls_names[:]
        else:
            completions = [ f
                            for f in cls_names
                            if f.startswith(text)
                            ]
        return completions

    def do_show(self, args):
        """
        Prints the string representation of an instance

        Usage: show [class name] [id]
        """

        if not args:
            print("** class name missing **")
            return

        try:  # test for second argument
            cls_name, cls_id = args.split(' ')
        except ValueError:
            print("** instance id missing **")
            return
        else:
            if cls_name != "BaseModel":
                print("** class doesn't exist **")
                return

        inst = cls_name + '.' + cls_id
        if inst in self.__instances:
            print(self.__instances[inst])
        else:
            print("** no instance found **")
        return




if __name__ == '__main__':
    HBNBCommand().cmdloop()
