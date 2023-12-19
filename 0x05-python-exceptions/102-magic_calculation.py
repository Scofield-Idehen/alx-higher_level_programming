#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception("Too far")
            else:
                result += a**b / idx
        except:
            result = b + a
            break
    return result
