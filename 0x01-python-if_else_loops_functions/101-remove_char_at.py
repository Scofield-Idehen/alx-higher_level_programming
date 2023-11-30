#!/usr/bin/python3
def remove_char_at(str, n):
    final_str = ""
    i = 0
    while i < len(str):
        if i != n:
            final_str += str[i]
        i += 1
    return final_str
