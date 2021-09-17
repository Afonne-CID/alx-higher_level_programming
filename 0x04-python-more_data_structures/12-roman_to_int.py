#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
    }
    cnt, value = 0, 0
    if (not isinstance(roman_string, str) or (len(roman_string)) == 0):
        return (0)

    for each in roman_string:
        cnt += 1
        for key in roman_values:
            if each == key:
                if cnt < len(roman_string):
                    if roman_string[cnt] in roman_values:
                        if roman_values[roman_string[cnt]] > roman_values[key]:
                            value += 0 - roman_values[key]
                        else:
                            value += roman_values[key]
                    else:
                        return (0)
                else:
                    value += roman_values[key]
    return (value)
