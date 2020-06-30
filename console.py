#!/usr/bin/env python3

"""
Write a class Base with prompt method
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
