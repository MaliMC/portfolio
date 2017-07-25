import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
#print(elementsList)
print(elementsList[0])

# print the last element
print(elementsList[int(len(elementsList)/2)])
# print all the elements


# Start your search algorithm here.
question = input("Is your name higher or lower than the second printed name: ")
if question == "lower":
        print(elementsList[0])
        print(elementsList[int(len(elementsList)//4)])
