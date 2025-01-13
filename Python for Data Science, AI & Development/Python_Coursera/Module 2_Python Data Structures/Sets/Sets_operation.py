#Sets Operation In Python

#Finding IUntersactions In Sets
set1={1,2,3,4,5,6,7}
Set2={4,5,6,7,8,9}
print(set1 & Set2)
print(set1.intersection(Set2))

#Finding Union Of Sets
print(set1 | Set2)
print(set1.union(Set2))

#Finding Difference of sets
print(set1-Set2)
print(set1.difference(Set2))

#Finding Symmetric Difference of sets
print(set1^Set2)
print(set1.symmetric_difference(Set2))

#We can also use update function to update sets which acts as like union
Set2.update(set1)
print(Set2)

# Python code to get the difference between two sets
# using difference_update() between set A and set B
 
# Driver Code
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
A.difference(B)
print (A)
print(A.difference(B))
# Modifies A and returns None
A.difference_update(B)

# Prints the modified set
print (A)

#Checck if two sets are disjoint if yes True Else False
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2)) #gives True as there is no common


#Check Subset
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1)) #Returns Truue as S2 elements are in S1

#Check superset
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print("A.issuperset(B) : ", A.issuperset(B)) #A is subset not a superset
print("B.issuperset(A) : ", B.issuperset(A)) #True as B has all elements in A

