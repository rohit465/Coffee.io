# Write a Python program to get the number of occurrences of a specified element in an
# array.
arr = [1,4,3,7,5]
i = 0
# creating empty arr of size 10 with value 0
a = [0]*10
while(i < len(arr)):
    a[arr[i]]=a[arr[i]]+1
    i=i+1

print(a)
