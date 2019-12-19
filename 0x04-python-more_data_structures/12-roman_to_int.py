#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_String, str) is False:
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    value = 0
    number = 'I'
    for i in roman_string[::-1]:
        if roman[i] >= roman[number]:
            value += roman[i]
            number = i
        else:
            value -= roman[i]
    return value
