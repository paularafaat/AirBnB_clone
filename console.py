#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Create a new instance of BaseModel and print its id"""
        if not arg:
            print("** class name missing **")
            return
        if arg == "BaseModel":
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance
        based on class name and id"""
        args = arg.split()
        objdict = storage.all()
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        else:
            class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in objdict.keys():
            print("** no instance found **")
            return
        print(objdict[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Deletes the instance from storage if it exists
        and saves the change into the storage."""
        args = arg.split()
        objdict = storage.all()
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        else:
            class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in objdict.keys():
            print("** no instance found **")
            return
        else:
            del objdict[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations
        of instances based on class name"""
        obj_dicts = storage.all()
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in obj_dicts.values()])
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in obj_dicts.items()
                   if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        obj_dicts = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in obj_dicts:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = obj_dicts[instance_key]
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** cannot update read-only attribute **")
            return
        setattr(instance, attribute_name, type(getattr(instance, attribute_name))(attribute_value))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
