#!/usr/bin/env python3

"""
Write a class Base with prompt method
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    doc_header = 'Documented commands (type help <topic>):'

    ruler = '='



    def do_prompt(self, line):

        """None"""
        HBNBCommand.prompt = line

    def do_EOF(self, line):
        """CTRL^D"""
        return True

    def do_quit(self, line):
        """Type "quit" to Quit"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
