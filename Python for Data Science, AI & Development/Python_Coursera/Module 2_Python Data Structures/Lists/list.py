#A list is a data structure in Python that allows you to store multiple items in a single variable. 
#It is ordered, mutable (can be changed), and can contain elements of different data types (integers, strings, floats, other lists, etc.).

# Examples of lists
# empty_list = []                 # An empty list
# numbers = [1, 2, 3, 4, 5]       # List of integers
# mixed = [1, "Hello", 3.5, True] # Mixed data types
# nested = [[1, 2], [3, 4]]       # Nested list (list of lists)

# print(numbers)  # Output: [1, 2, 3, 4, 5]
# print(mixed)  # Output: [1, 'Hello', 3.5, True]
# print(empty_list)
# print(nested)

#Indexing and Slicing in Python
name=["Bhuwan", "Aakriti", "rajan", "Chiso"]
print(name)
print(name[0])
print(name[-2]) #list elements are indexed from 0 at start and  negative -1 from last

#Slicing In Python
numbers = [10, 20, 30, 40, 50]

# Slicing a list
print(numbers[1:4])  # Output: [20, 30, 40]
print(numbers[:3])   # Output: [10, 20, 30] (start is 0 by default)
print(numbers[3:])   # Output: [40, 50] (end is last by default)
