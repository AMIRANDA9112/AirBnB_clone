#!/usr/bin/env python3
"""
Write a class Console for nBnB
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """interpreter the comands"""

    prompt = '(hbnb)'

    ___classObj = [
        "BaseModel", "User", "State", "Amenity",
        "Place", "Review", "City"]

    def do_create(self, arg):
        """create instance """
        if arg == "":
            print("** class name missing **")
        else:
            if arg not in HBNBCommand.___classObj:
                print("** class doesn't exist **")
            else:
                obj = arg + '()'
                my_model = eval(obj)
                my_model.save()
                print(my_model.id)

    def do_show(self, arg):
        """show the instance"""
        if arg == "":
            print("** class name missing **")
        else:
            token = arg.split(' ')
            if token[0] not in HBNBCommand.___classObj:
                print("** class doesn't exist **")
            else:
                if len(token) > 1:
                    key = "{}.{}".format(token[0], token[1])
                    all_objt = storage.all()

                    for id, value in all_objt.items():
                        if id == key:
                            print(value.__str__())
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_destroy(self, arg):
        """destroy instance"""
        if arg == "":
            print("** class name missing **")
        else:
            token = arg.split(' ')
            if token[0] not in HBNBCommand.___classObj:
                print("** class doesn't exist **")
            else:
                if len(token) > 1:
                    key = "{}.{}".format(token[0], token[1])
                    all_objt = storage.all()
                    for id in all_objt.keys():
                        if id == key:
                            del all_objt[key]
                            storage.save()
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_all(self, arg):
        """print all object string the a class"""
        all_objt = storage.all()
        list_objt = []
        if len(arg) == 0:
            storage.reload()
            for k, v in all_objt.items():
                list_objt.append(v.__str__())
                print(list_objt)
            return

        if arg not in HBNBCommand.___classObj:
            print("** class doesn't exist **")
        else:
            for k, v in all_objt.items():
                dict_obj = v.__str__()
                if v.__class__.__name__ == arg:
                    list_objt.append(v.__str__())

            print(list_objt)

    def do_update(self, arg):
        """update data instance"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            token = arg.split(' ')

            if token[0] not in HBNBCommand.___classObj:
                print("** class doesn't exist **")
            else:
                if len(token) > 1:
                    key = "{}.{}".format(token[0], token[1])
                    storage.reload()
                    all_objt = storage.all()
                    for k, v in all_objt.items():

                        if k == key:
                            if len(token) == 2:
                                print("** attribute name missing **")
                                return
                            elif len(token) == 3:
                                print("** value missing **")
                                return
                            else:
                                if hasattr(v, token[2]):
                                    pass
                                else:
                                    v.__dict__[token[2]] = token[3]
                                    storage.save()
                                return

                    print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_EOF(self, arg):
        """End of file function """
        return True

    def do_quit(self, arg):
        """Salir del interprete"""
        return(True)

    def emptyline(self):
        """No realiza ninguna accion"""
        pass

    def default(self, arg):
        token = arg.split('.')
        if token[0] in HBNBCommand.___classObj and token[1] == "all()":
            self.do_all(token[0])
        else:
            print("Error: comando inexistente")


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
