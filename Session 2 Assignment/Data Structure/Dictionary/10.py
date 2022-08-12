# Write a Python program to count the values associated with key in a
# dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
# False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

test_dict =[{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
 
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
 
# Initialize value
K = True
 
# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == True:
        res = res + 1
     
# printing result
print("Frequency of K is : " + str(res))