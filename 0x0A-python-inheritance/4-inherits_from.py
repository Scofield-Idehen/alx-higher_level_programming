#!/usr/bin/python3
"""Write imported module here"""


def inherits_from(obj, a_class):
    """Func dat check if obj is an inst of class that inherited
    Args:
        obj: the object
        a_class: givin class

    Return: True otherwise False
    """
    obj_class = type(obj)

    if issubclass(obj_class, a_class) and obj_class != a_class:
        return True
    else:
        return False
