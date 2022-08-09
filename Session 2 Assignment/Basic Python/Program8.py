# Write a Python program to create a histogram from a given list of integers.

a = [1,2,5,4,34]

for n in a:
    histogrm = ''
    times = n
    while(times > 0):
        histogrm += "#"
        times-=1

    print(histogrm)
