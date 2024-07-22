# Write a python program for factorial of number using recursion

n=int(input('Enter the value of n: '))
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(n))