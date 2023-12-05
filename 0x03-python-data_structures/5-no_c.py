#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for idx in range(len(my_string)):
        if my_string[idx] != "c" and my_string[idx] != "C":
            new_string += my_string[idx]
    return new_string
