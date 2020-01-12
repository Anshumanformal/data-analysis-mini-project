"""
Name: Python Data Analysis
Purpose: Read CSV File and store data in dictionary

Algorithm:

Step 1: Opening File in read mode and looping through data
Step 2: Printing the data just to ensure successful read

"""

import os

print("A Simple Data Analysis Program")
print()

d1 = {}

with open(os.path.join(r'<YOUR FILE LOCATION HERE>','Emissions.csv'), 'r') as file:
    # Read in file object and splitting it with '\n'
    f1 = file.read().split('\n')
    for data in f1:
        # Updating the dictionary file | Splitting the string by COMMA(,) - Store first value as KEY
        # and Store other value as VALUE
        a1 = data.split(',')[0]     # data is itself a list coming from f1.
        a2 = data.split(',')[1:]    # data is itself a list coming from f1.
        d1.update({ a1: a2})
        
for x, y in d1.items():
    print(x, end=" - ")
    print(y)

print()
print("All data from Emissions.csv has been read into a dictionary.")
