# Write the program in python to calculate cubic sum of first n natural numbers using recursion

def sumOfSeries(n):
    #code here
    return (n*(n+1)//2)**2 #This code for higer inpupt

# For lower input

def sumOfSeries2(n):
    if n==1:
        return 1
    return n*n*n + sumOfSeries2(n-1)

print(sumOfSeries(100))

print(sumOfSeries2(100))