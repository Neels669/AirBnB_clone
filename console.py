#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class defines the cmd"""
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

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

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg == '':
            print("** class name missing **")
            return
        y = arg.split()
        if y[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(y) == 1:
            print("** instance id missing **")
            return
        key = y[0] + "." + y[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(y) == 2:
            print("** attribute name missing **")
            return
        q = arg.split('"')
        if len(q) == 1:
            print("** value missing **")
            return
        attr = y[2]
        try:
            value = getattr(objects[key], attr)
            t = type(value)
            setattr(objects[key], attr, t(q[1]))
        except AttributeError:
            setattr(objects[key], attr, q[1])
        storage.save()

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

    def do_create_user(self, arg):
        """Creates a new instance of User"""
        if arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                new_user = User()
                new_user.save()
                print(new_user.id)

    def do_show_user(self, arg):
        """Shows an instance of User"""
        if arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    user_id = args[1]
                    key = "User." + user_id
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")

    def do_destroy_user(self, arg):
        """Destroys an instance of User"""
        if arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    user_id = args[1]
                    key = "User." + user_id
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all_user(self, arg):
        """Lists all User instances"""
        if arg == '':
            objects = storage.all()
            user_instances = [str(obj) for key,
                              obj in objects.items() if "User." in key]
            print(user_instances)
        else:
            print("** class doesn't exist **")

    def do_update_user(self, arg):
        """Updates an instance of User"""
        if arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    user_id = args[1]
                    key = "User." + user_id
                    objects = storage.all()
                    if key not in objects:
                        print("** no instance found **")
                    else:
                        if len(args) == 2:
                            print("** attribute name missing **")
                        elif len(args) == 3:
                            print("** value missing **")
                        else:
                            attribute_name = args[2]
                            attribute_value = args[3]
                            setattr(objects[key],
                                    attribute_name, attribute_value)
                            objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
