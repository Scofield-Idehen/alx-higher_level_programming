#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    # define a dic with the numerals
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = rom_num[char]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value

    return result
