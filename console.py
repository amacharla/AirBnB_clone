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

# ==================== setup ====================

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

# ==================== Commands ====================

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

    def do_show(self, args):
        """
        Prints the string representation of an instance

        Usage: show [class name] [id]
        """

        if not args:  # if no arguments are passed
            print("** class name missing **")
            return

        try:  # testing arguments
            cls_name, cls_id = args.split(' ')
            _ = eval(cls_name)()
        except ValueError:  # test for second argument
            print("** instance id missing **")
            return
        except NameError:  # test if class exist
            print("** class doesn't exist **")
            return

        inst = cls_name + '.' + cls_id
        if inst in self.__instances:  # check if instance exist
            print(self.__instances[inst])  # get obj
        else:
            print("** no instance found **")
        return

    def do_destroy(self, args):
        """
        Deletes an instance and saves the changes into JSON file

        Usage: destroy [class name] [id]
        """

        if not args:  # if no arguments are passed
            print("** class name missing **")
            return

        try:  # testing arguments
            cls_name, cls_id = args.split(' ')
            _ = eval(cls_name)()
        except ValueError:  # test for second argument
            print("** instance id missing **")
            return
        except NameError:  # test if class exist
            print("** class doesn't exist **")
            return

        inst = cls_name + '.' + cls_id
        if inst in self.__instances:  # check if instance exist
            del self.__instances[inst]  # delete obj
            storage.save()  # save changes into JSON file
        else:
            print("** no instance found **")

        return

    def do_all(self, cls_name):
        """
        Prints all string representation of all or class instances

        Usage: all [(class name)]
        """

        result = ['[']
        trigger = 0 if cls_name else 1

        for obj in storage.all().values():
            if trigger or obj.__class__.__name__ == cls_name:
                result.append(str(obj) + '\n')

        result = "".join(result)
        print(result[:-1] + ']')

# ==================== AUTO-COMPLETION  ====================

    def complete_create(self, text):
        """ Auto-complete for `create` """

        instances = list(self.__instances.keys())  # list of instances
        # get only the class name and strip the id away in `class.id`
        # all options for class names
        cls_names = list(set((name.split('.')[0] for name in instances)))
        if not text:  # when usr press tab wihtout txt.
            completions = cls_names[:]  # show all options
        else:  # auto complete usr press tab
            completions = [ letters
                            for letters in cls_names
                            if letters.startswith(text)
                          ]
        return completions

    def complete_show(self, text, line):
        """ Auto-complete for `show` """

        instances_key = list(self.__instances.keys())  # instances list format
        # turn `class.id` -> `class id`
        instances = list(set((name.replace('.',' ') for name in instances_key)))

        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in instances if s.startswith(mline)]

    def complete_destroy(self, text, line):
        """ Auto-complete for `destroy` """

        instances_key = list(self.__instances.keys())  # instances list format
        # turn `class.id` -> `class id`
        instances = list(set((name.replace('.',' ') for name in instances_key)))

        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in instances if s.startswith(mline)]

    def complete_all(self, text):
        """ Auto-complete for `create` """

        instances = list(self.__instances.keys())  # list of instances
        # get only the class name and strip the id away in `class.id`
        # all options for class names
        cls_names = list(set((name.split('.')[0] for name in instances)))
        if not text:  # when usr press tab wihtout txt.
            completions = cls_names[:]  # show all options
        else:  # auto complete usr press tab
            completions = [ letters
                            for letters in cls_names
                            if letters.startswith(text)
                          ]
        return completions

if __name__ == '__main__':
    HBNBCommand().cmdloop()
