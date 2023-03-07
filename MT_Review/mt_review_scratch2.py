"""

CS210 Exam 2 Review Scratch Code
Author: Jose Renteria

"""


def func(i: int):
    for el in range(i):
        el += i
    return el


print(func(6))

print("-" * 15)

s1 = 'literal'
s2 = ['l', 'i', 't', 'e', 'r', 'a', 'l']

print(s2.sort())  # sort alphabetically

print(1 if 'litrla' in s1 and s2 else 0)

print("-" * 15)

t1 = 'ba'
t2 = ['a', 'b']
print((t1.index('b')), (t2.index('b')))
print(min(t1) == min(t2))

print("-" * 15)

v1 = ["kg", "to", "lbs"]
print("_".join(v1))

print("-" * 15)


def char_exist(vals: str, c: str) -> bool:
    return c in vals # is char in str


print(char_exist("gumbo", 'b'))

print("-" * 15)


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

<<<<<<< HEAD

with open("sample.txt", 'r') as sample:
    print(sample.read(2))  # first two characters only

lst = [1,2,3]
lst[0] = 2
print(lst)


s = "1234"
print(s, type(s))
s = (s)
print(type(s))
=======
with open("sample1.txt", 'x') as f:
    f.write("this is a new file")
>>>>>>> d4320c8a907087dbb9fac4a46143edc476f56572
