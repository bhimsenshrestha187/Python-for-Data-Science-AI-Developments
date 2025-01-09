#A list is a mutable (changeable) and ordered sequence of items. 
# It can store elements of different data types, including integers, floats, strings, and even other lists.
#It is mutable, ordered and heterogeneous.
#Lists are created using square brackets [].\
#since list are mutable, we can use clone of list to create new list by changing a element without affecting old list.
#Such things are not possible in tupple as tupples are immutable.

A=["nepal", "india", 1]
B=A[:] #Cloning A
B[0]="China"
print(B)

# Examples of lists
# empty_list = []                 # An empty list
# numbers = [1, 2, 3, 4, 5]       # List of integers
# mixed = [1, "Hello", 3.5, True] # Mixed data types
# nested = [[1, 2], [3, 4]]       # Nested list (list of lists)

#We can use expend to add elements in list and appensd to add only one element.A

name=["bhimnsen", "Hari","Shiva"]
name.extend(["Game","Fame"])
print(name)
name.append(["parvati","garima"])
print(name)

my_list = [10, 20, 30, 40, 50] 
my_list.remove(30) # Removes the element 30 ,here remove method is used to remove only one elementor first occurance in list.
print(my_list) 

