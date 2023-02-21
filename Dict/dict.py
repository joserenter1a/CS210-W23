"""
CS210 Class Encore 
Author: Jose Renteria

Practice with dictionaries and File I/O. 

"""
# We can initialize a dict like this, similar to JSON notation
mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'mileage': 89_000
}

# But in Python, dictionaries cannot store duplicates on a single key, for example:
mustang['model'] = 'F150' # this will overwrite the model
print(mustang)

mustang.update({'model': 'Mustang'}) # can also be done like this
print(mustang)

# but lets say you are an auto dealer, you obviously carry more than one model
# lets say you also have a F150 and a Bronco currently

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
    pass # Delete when you start writing
    # TODO
    # assign the reader object, with your file passed into it, to a var called 'csv_reader'
    # skips onto the next iteration in the object i.e. line 2 if starting at line 1

    # iterate over your objet, your csv_reader is a collection of lines aka an ITERABLE
    # initialize all our variables in each line, read the file to know what they are

    # if the key exists
    # add it to the list with the key
    # create a key and assign it the first value

    #print((new_dict)) # entire dictionary
    #print(new_dict.keys())  # all the keys
