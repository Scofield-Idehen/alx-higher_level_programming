#!/usr/bin/python3
"""Write imported module here"""


def is_same_class(obj, a_class):
    """Func dat check if object is exactly and instance of given class
    Args:
        obj: the object to check
        a_class: class

    Return: True odawise False
    """
    return type(obj) == a_class
