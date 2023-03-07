"""
CS210 Class Encore 
Author: Jose Renteria

Practice with dictionaries and File I/O. 

"""
# We can initialize a dict like this, similar to JSON notation
mustang = {
<<<<<<< HEAD

=======
>>>>>>> d4320c8a907087dbb9fac4a46143edc476f56572
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'mileage': 89_000
<<<<<<< HEAD

=======
>>>>>>> d4320c8a907087dbb9fac4a46143edc476f56572
}
# Iterable types
# things that can be iterated over, containers, store multiple values, that you can access later
# dict, lists, tuples, sets, csv.reader, File

car = {"mustang": [2010, 2011, 2012]}

# O(1)

# But in Python, dictionaries cannot store duplicates on a single key, for example:
mustang['model'] = 'F150' # this will overwrite the model
print(mustang)

mustang.update({'model': 'Mustang'}) # can also be done like this
print(mustang)

# but lets say you are an auto dealer, you obviously carry more than one model
# lets say you also have a F150 and a Bronco currently
<<<<<<< HEAD


F150 = {
  "brand": "Ford",
  "model": "F150",
  "year": 2009,
  "mileage": 100_029
}

Bronco = {
  "brand": "Ford",
  "model": "Bronco",
  "year": 2023,
  "mileage": 1220
}
<<<<<<< HEAD
=======

=======

F150 = {
  "brand": "Ford",
  "model": "F150",
  "year": 2009,
  "mileage": 100_029
}

Bronco = {
  "brand": "Ford",
  "model": "Bronco",
  "year": 2023,
  "mileage": 1220
}

>>>>>>> d4320c8a907087dbb9fac4a46143edc476f56572
>>>>>>> d6381220a0070c5cada286da511d9c7988c5c30b
models = [mustang, F150, Bronco] # These are the current models offered
lot = {}                         # initialize an empty lot
key = 'Current Models Available' # what we want our key to be
for model in models:            # iterate through the current models we want to store in our dict
    if key in lot:              # if the key already exists,
        lot[key].append(model)  # we simply append the model to the key
    else:
        lot[key] = [model]      # if not, initialize the key, and assign its 
                                # value a LIST with the first model inside of that list, aka the Mustang
print(lot)


"""
Now, time to do it on your own

We want to create a dictionary of students, and have the keys be their class standing
So if I call student_dict['Freshman'], I want to see all Freshmen in the system listed

"""


import csv  # import our csv module

student_dict = {} # Initialize an empty dict

with open('names.csv', 'r') as csv_file:  # we use 'with' so it can handle opening and closing the file
<<<<<<< HEAD

    csv_reader = csv.reader(csv_file)
=======
<<<<<<< HEAD
    pass
    # TODO

    csv_reader = csv.reader(csv_file)
    # assign the reader object, with your file passed into it, to a var called 'csv_reader'
    # skips onto the next iteration in the object i.e. line 2 if starting at line 1
    next(csv_reader)
    # iterate over your object, your csv_reader is a collection of lines aka an ITERABLE
    # (name, age, standing) == (0, 1, 2)

    for line in csv_reader:
        name, age, standing = line
    # initialize all our variables in each line, read the file to know what they are
    # if the key exists
        if standing in student_dict:
            student_dict[standing].append((name, int(age)))
        else:
            student_dict[standing] = [(name, int(age))]
    # add it to the list with the key
    # create a key and assign it the first value

    print((student_dict.keys()))
=======
    pass # Delete when you start writing
    # TODO
>>>>>>> d6381220a0070c5cada286da511d9c7988c5c30b
    # assign the reader object, with your file passed into it, to a var called 'csv_reader'
    # skips onto the next iteration in the object i.e. line 2 if starting at line 1
    next(csv_reader)
    # iterate over your object, your csv_reader is a collection of lines aka an ITERABLE
    # (name, age, standing) == (0, 1, 2)

    for line in csv_reader:
        name, age, standing = line
    # initialize all our variables in each line, read the file to know what they are
    # if the key exists
        if standing in student_dict:
            student_dict[standing].append((name, int(age)))
        else:
            # standing would be Senior
            student_dict[standing] = [name, int(age)]
    # add it to the list with the key
    # create a key and assign it the first value
<<<<<<< HEAD
    print((student_dict.keys()))
=======

    #print((new_dict)) # entire dictionary
    #print(new_dict.keys())  # all the keys
>>>>>>> d4320c8a907087dbb9fac4a46143edc476f56572
>>>>>>> d6381220a0070c5cada286da511d9c7988c5c30b
