#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the cmd"""
    prompt = "(hbnb) "

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
