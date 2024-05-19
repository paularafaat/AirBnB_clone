#!/usr/bin/python3
"""console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quiting the console"""
        return True

    def help_quit(self):
        """Help information for the quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Handle EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
