#!/usr/bin/python3
"""Defines a class Stu."""


class Student:
    """Represent a stu."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the stu.
            last_name (str): The last name of the stu.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Stu."""
        return self.__dict__
