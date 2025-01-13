#basic Operation in sets

#add elements in sets
my_set={"A",5,2,3,6,1}
my_set.add(4) #add elements in sets
print(my_set)

#Removing Elements from Sets
my_set.remove(4) #removes 4
my_set.discard(5) #Though 5 not is in set, it doenst give error.
print(my_set)
my_set.pop()
print(my_set) #

#clearing and deleting sets
my_set.clear() #Clears all the elements in sets and Give an empty sets.
print(my_set)

set2={4,5,6,8}
print(set2)
del set2 #Delete the entire set and displays error when we try to access it
# print(set2)



# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)

