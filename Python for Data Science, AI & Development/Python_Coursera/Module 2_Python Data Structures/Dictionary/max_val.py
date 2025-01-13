#ython programme to fine keys with maximum values
#Using For Loop
#create a dictionary
d = {'CS': 2, 'Gfg': 2, 'for': 1}
 
# get the maximum value in the dictionary
max_val = max(d.values())
 
# create a list to store the keys with maximum values
max_keys = []
 
# loop through the dictionary
for key in d:
 
    # check if the value of the current key is equal to the maximum value
    if d[key] == max_val:
         
        # append the key to the list of max keys
        max_keys.append(key)
 
# print the keys with maximum values
print("Keys with maximum values are :", max_keys)





# Python3 code to demonstrate working of
# Keys with Maximum value
# Using max() + list comprehension + values()
 
# initializing dictionary
test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Using max() + list comprehension + values()
# Keys with Maximum value
temp = max(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]
 
# printing result 
print("Keys with maximum values are : " + str(res))