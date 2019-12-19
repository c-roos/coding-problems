# Repeated Elements in a Character Array
#
# Given an array of characters, identify the first repeated character in the array.


def first_repeat(l):
    present = {}
    for char in l:
        if present.get(char):
            return char
        present[char] = 1
    return None
