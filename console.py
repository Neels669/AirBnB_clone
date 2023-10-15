#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class defines the cmd"""
    classes = ["BaseModel"]

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg == '':
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance"""
        if arg == '':
            print("** class name missing **")
        else:
            x = arg.split()
            if x[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = x[0] + "." + x[1]
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == '':
            print("** class name missing **")
        else:
            x = arg.split()
            if x[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = x[0] + "." + x[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        if arg == '':
            objects = storage.all()
            z = []
            for v in objects.values():
                z.append(str(v))
            print(z)
        elif arg in HBNBCommand.classes:
            objects = storage.all()
            z = []
            for v in objects.values():
                if v.__class__.__name__ == arg:
                    z.append(str(v))
            print(z)
        else:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def help(self):
        """Show help message"""
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit\n")

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")
        pass

    def help_EOF(self):
        """EOF command to exit the program"""
        print("EOF command to exit the program")
        pass

    def help_help(self):
        """Help command to get help on the program"""
        print("Help command to get help on the program")
        pass

    def emptyline(self):
        """Handle an empty line (ENTER key) without executing any action"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
