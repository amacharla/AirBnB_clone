#!/usr/bin/python3
"""
Entry point of the command interpreter
AirBnB Version 1
"""
import cmd
from models import storage, obj_constructor
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command Line Class """

# ==================== setup ====================

    prompt = "(hbhb) "
    __instances = storage.all()  # used for auto-completion

    def do_quit(self, line):
        """ Exits the HBNB Console """
        quit()

    def do_EOF(self, line):
        """If a command handler returns true value, program will exit clean """
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
                instance = obj_constructor(cls_name, 1)
            except NameError:
                print("** class doesn't exist **")
            else:
                print(instance.id)
                instance.save()  # save instance to JSON file
                self.__instances = storage.all()  # update inst autocomplete
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
            obj_constructor(cls_name)
        except ValueError:  # test for second argument
            print("** instance id missing **")
            return
        except NameError:  # test if class exist
            print("** class doesn't exist **")
            return

        inst = cls_name + '.' + cls_id
        instances = storage.all()
        if inst in instances:  # check if instance exist
            print(instances[inst])  # get obj
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
            obj_constructor(cls_name)
        except ValueError:  # test for second argument
            print("** instance id missing **")
            return
        except NameError:  # test if class exist
            print("** class doesn't exist **")
            return

        inst = cls_name + '.' + cls_id
        if inst in storage.all():  # check if instance exist
            del storage.all()[inst]  # delete obj
            storage.save()  # save changes into JSON file
            self.__instances = storage.all()  # update inst for autocomplete
        else:
            print("** no instance found **")

        return

    def do_all(self, cls_name):
        """
        Prints all string representation of all or class instances

        Usage: all [(class name)]
        """

        result = ['[']
        trigger = 0 if cls_name else 1  # if optional argument was passed

        if not trigger:
            try:  # check if class exist
                obj_constructor(cls_name)
            except:
                print("** class doesn't exist **")
                return

        for obj in storage.all().values():
            if trigger or obj.__class__.__name__ == cls_name:
                result.append(str(obj) + '\n')

        result = "".join(result)
        if len(result) == 1:  # if no instances exist, send empty '[]'
            result += ']'

        print(result[:-1] + ']')  # last '\n' will be overwritten with ']'

    def do_update(self, args):
        """
         Updates an instance based on the class name and id

         Usage: update <class name> <id> <attribute name> "<attribute value>"
         """

        if not args:  # testing arguments are passed
            print("** class name missing **")
            return

        args = args.split()

        if len(args) >= 1:
            try:  # testing `class` argument
                obj_constructor(args[0])
            except NameError as error:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")

        if len(args) < 2:  # testing `id` argument
            print("** instance id missing **")
            return
        else:
            inst = args[0] + '.' + args[1]  # `class.id`
            instances = storage.all()
            if inst in instances:  # get obj
                obj = instances[inst]
            else:
                print("** no instance found **")
                return

        if len(args) < 3:  # testing `attribute` argument
            print("** attribute name missing **")
            return
        elif args[2] in "id, created_at, updated_at":  # shouldnt modify
            return
        else:
            if len(args) < 4:  # testing `value` argument
                print("** value missing **")
                return
            else:  # strip the quotes
                args[3] = args[3].strip('\"')

        setattr(obj, args[2], args[3])  # update instance
        obj.save()  # save updated obj
        return

    def do_BaseModel(self, args):
        """retrieving instances of class"""
        self.inst_class('BaseModel', args)

    def do_User(self, args):
        """retrieving instances of class"""
        self.inst_class('User', args)

    def do_State(self, args):
        """retrieving instances of class"""
        self.inst_class('State', args)

    def do_City(self, args):
        """retrieving instances of class"""
        self.inst_class('City', args)

    def do_Amenity(self, args):
        """retrieving instances of class"""
        self.inst_class('Amenity', args)

    def do_Place(self, args):
        """retrieving instances of class"""
        self.inst_class('Place', args)

    def do_Review(self, args):
        """retrieving instances of class"""
        self.inst_class('Review', args)

    def inst_class(self, cls_name, args):
        """Helper method"""
        if '.all()' in args:
            self.do_all(cls_name)

# ==================== AUTO-COMPLETION  ====================
    def complete_create(self, text, line, begidx, endidx):
        """ Auto-complete for `create` """
        instances_key = list(self.__instances.keys())  # list of instances
        # get only the class name and strip the id away in `class.id`
        # all unique options for class names
        cls_names = list(set((name.split('.')[0]
                              for name in instances_key)))
        if not text:  # when usr press tab wihtout txt.
            completions = cls_names[:]  # show all options
        else:  # auto complete usr press tab
            completions = [letters
                           for letters in cls_names
                           if letters.startswith(text)]
        return completions

    def complete_show(self, text, line, begidx, endidx):
        """ Auto-complete for `show` """

        instances_key = list(self.__instances.keys())  # instances list format
        # turn `class.id` -> `class id`; only show unique class names
        instances = list(set((name.replace('.', ' ')
                              for name in instances_key)))

        # taken from Stack Overflow
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in instances if s.startswith(mline)]

    def complete_destroy(self, text, line, begidx, endidx):
        """ Auto-complete for `destroy` """

        instances_key = list(self.__instances.keys())  # instances list format
        # turn `class.id` -> `class id`; only show unique class names
        instances = list(set((name.replace('.', ' ')
                              for name in instances_key)))

        # taken from Stack Overflow
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in instances if s.startswith(mline)]

    def complete_all(self, text, line, begidx, endidx):
        """ Auto-complete for `create` """

        instances_key = list(self.__instances.keys())  # list of instances
        # get only the class name and strip the id away in `class.id`
        # all unique options for class names
        cls_names = list(set((name.split('.')[0]
                              for name in instances_key)))
        if not text:  # when usr press tab wihtout txt.
            completions = cls_names[:]  # show all options
        else:  # auto complete usr press tab
            completions = [letters
                           for letters in cls_names
                           if letters.startswith(text)]
        return completions

    def complete_update(self, text, line, begidx, endidx):
        """ Auto-complete for `update` """

        instances_key = list(self.__instances.keys())  # instances list format
        # turn `class.id` -> `class id`; only show unique class names
        instances = list(set((name.replace('.', ' ')
                              for name in instances_key)))

        # taken from Stack Overflow
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in instances if s.startswith(mline)]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
