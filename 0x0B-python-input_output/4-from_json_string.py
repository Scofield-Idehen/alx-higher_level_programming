#!/usr/bin/python3
"""Defines a JSON-to-object func"""
import json


def from_json_string(my_str):
    """Ret the Python obj representation of a JSON string."""
    return json.loads(my_str)
