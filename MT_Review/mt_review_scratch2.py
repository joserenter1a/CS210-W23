"""

CS210 Exam 2 Review Scratch Code
Author: Jose Renteria

"""

def func(i: int):
    for el in range(i):
        el += i
    return el

print(func(6))

s1 = 'literal'
s2 = ['l', 'i', 't', 'e', 'r', 'a', 'l']
(s2.sort())
s1.sort()
print(s2)
print(1 if 'liter' in s1 and s2 else 0) 

t1 = 'ba'
t2 = ['a', 'b']
print(min(t1) == min(t2))

v1 = ["kg", "to", "lbs"]
print("_".join(v1))


def char_exist(vals: str, c: char) -> bool:
    return c in vals
print(char_exist("gumbo", 'b'))


def remove_duplicates(string):
    # Initialize an empty string to accumulate unique characters
    unique = ""

    # Iterate over each character in the string
    for char in string:
        # If the character is not already in the unique_chars string,
        # add it to the string
        if char not in unique:
            unique += char

    # Return the accumulated string with duplicates removed
    return unique

with open("sample.txt", 'r') as sample:
    print(sample.readlines())