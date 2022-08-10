# Write a Python program to reverse the order of the items in the array
arr = [1,2,3,4,5,6]
i = 0
# print(len(arr))
while(i <= len(arr)/2):
    temp = arr[i]
    arr[i] = arr[len(arr)-i-1]
    arr[len(arr)-i-1] = temp
    i=i+1

print(arr)