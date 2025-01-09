#Tuples are created using parentheses ().
#Square brackett is used for indexing.
# Tuples are immutable meanings its element cannot be changed or modified. 
#Since tuples are immutable, we can sort elements of tupple and save to new tuples
# This make them faster and more memory efficient than lists.
#Items in tuples are sorted in a defined sequence.
#A tuple can hold multiple data types (e.g., integers, strings, lists, or even other tuples).
#Tuples can contain other tuples, creating a nested structure.
# If we manuplate a tuple, we have to create new tuples.
#A tuple can contains other tupples within it.\
# When we sort tuple using sorted function, it gives results inside square bracket.

    
ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
a=sorted(ratings)
print(a)

# Print element on each index, including nest indexes
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])




# A=("nepal", "india", 1)
# B=A
# B[0]="China"
# print(A)
