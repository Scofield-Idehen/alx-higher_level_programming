#!/usr/bin/python3
"""MyList class modules"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Func dat prints list, in sorted (ascending sort)"""
        print(sorted(self))
