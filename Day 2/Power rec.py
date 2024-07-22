# Write a python program to find power of a given number using reccursion

def power(n,e):
    if e==0:
        return 1
    return n*power(n,e-1)

n,e=map(int,input('Enter number and powers: ').split())
print(power(n,e))