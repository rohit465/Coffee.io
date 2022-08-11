# Write a Python program to remove a key from a dictionary.
dict = {1:"hello", 5:"helllo", 3:"heello"}
print(dict)
del dict[1]
print(dict)
# other ways to delete the item from dictionary
# del dict[1]
dict.pop(3)
print(dict)