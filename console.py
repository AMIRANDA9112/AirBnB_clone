#!/usr/bin/env python3

"""
Write a class Base with prompt method
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    doc_header = 'Documented commands (type help <topic>):'

    ruler = '='


    def do_EOF(self, line):
        """Ctrl^C command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
