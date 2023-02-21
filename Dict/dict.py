import csv  # import our csv module

with open('names.csv', 'r') as csv_file:  # we use with so it can handle opening and closing the file
    csv_reader = csv.reader(csv_file)  # assigns the reader object to a var called 'csv_reader'

    next(csv_reader)  # skips onto the next iteration in the file i.e. line 2 if starting at line 1
    for line in csv_reader:  # standard loop structure, your csv_reader is a collection of lines
        name, class_standing = (line[0], line[2])  # assigns elements from your line[] at given indexes to a variable
        # print(name, class_standing)

        new_dict = {class_standing: name}  # assigns the key value pair

        print(new_dict)  # Prints the dict with the keys as the class standing


        # importance of a key, value pair

