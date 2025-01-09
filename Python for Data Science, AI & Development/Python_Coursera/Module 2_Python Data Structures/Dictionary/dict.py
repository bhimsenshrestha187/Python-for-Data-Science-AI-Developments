#A dictionary consists of keys and values.
#It is helpful to compare a dictionary to a list. 
#Instead of being indexed numerically like a list, dictionaries have keys. 
#These keys are the keys that are used to access values within a dictionary.
#An empty dictionary without any items is written with just two curly braces, like this "{}"
#Each key is separated from its value by a colon ":"
#For every key, there can only be one single value, however, multiple keys can hold the same value. 
#Keys can only be strings, numbers, or tuples, but values can be any data type.




# A dictionary representing a person's information
person = {
    "name": "Alice",        # key: "name", value: "Alice"
    "age": 25,              # key: "age", value: 25
    "city": "New York"      # key: "city", value: "New York"
}

# Accessing values using keys
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25

# Adding a new key-value pair
person["job"] = "Engineer"

# Modifying an existing value
person["age"] = 26

# Removing a key-value pair

# Checking the dictionary after modifications
print(person)
