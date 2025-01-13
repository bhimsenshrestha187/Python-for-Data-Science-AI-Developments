

#Using Len() Function
d ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}
print(len(d))

#Using List Comprehension
d = {"a": 1, "b": 2, "c": 3}
length = len([key for key in d])
print(length)

#Using sum() with 1 for each item
d = {"a": 1, "b": 2, "c": 3}
length = sum(1 for i in d)
print(length)

#Getting length of nested dictionary
d = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Alice", "age": 30},
    "person3": {"name": "Bob", "age": 22}
}
length = len(d)
print(length)