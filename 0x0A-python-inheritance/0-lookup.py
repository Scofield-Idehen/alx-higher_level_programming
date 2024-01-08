#!/usr/bin/python3
"""Write imported mod here"""


def lookup(obj):
    """function that ret list of available attrs and mthds of an obj

    Args:
        obj: the object wto lookup
    Returns:
        list of available attr and mthds"""
    return dir(obj)
