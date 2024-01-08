#!/usr/bin/python3
"""Write imported module here"""


def is_kind_of_class(obj, a_class):
    """Func dat checks if obj is of a sublass of a_class
    Args:
        obj: the object
        a_class: givin class

     Return: True otherwise False
    """
    return isinstance(obj, a_class)
