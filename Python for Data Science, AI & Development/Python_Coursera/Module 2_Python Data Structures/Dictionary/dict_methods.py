student = {"name": "Bhimsen", "age": 25, "major": "CS"}

# Keys, Values, Items
print(student.keys())   # Output: dict_keys(['name', 'age', 'major'])
print(student.values()) # Output: dict_values(['John', 25, 'CS'])
print(student.items())  # Output: dict_items([('name', 'John'), ('age', 25), ('major', 'CS')])

# Update
new_info = {"age": 26, "grade": "A"}
student.update(new_info)
print(student)  # Output: {'name': 'John', 'age': 26, 'major': 'CS', 'grade': 'A'}

for key, value in student.items():
    print(f"{key}: {value}")