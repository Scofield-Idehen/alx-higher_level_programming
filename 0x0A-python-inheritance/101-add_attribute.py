#!/usr/bin/python3
"""Write imported module here"""


def add_attribute(obj, name, value):
    """Func that add attributes

        Args:
        name: name to add
        value: val to add

      Raises:
            TypeError: if name or val cannot be added
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    elif hasattr(obj, "__slots__") and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
