#!/usr/bin/python3
"""class module"""


class LockedClass:
    """locking the __slots__. Return just the first_name attribute"""
    __slots__ = 'first_name'
