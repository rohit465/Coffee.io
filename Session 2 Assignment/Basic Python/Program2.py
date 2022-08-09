#  Write a Python program which accepts a sequence of comma-separated numbers from the
# user and generates a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')



Numbers = input("Input some comma seprated numbers : ")
list = Numbers.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)