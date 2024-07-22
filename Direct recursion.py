# Write a python program for printing n to 1 sequence
n = int(input("Enter the value of n: "))
def nto1(n):
    print(n)
    if n==1:
        return
    return nto1(n-1)
nto1(n)

# Format of direct recurisve code
'''
def func():
   base condn:
     return
    # Code
    return (recursive calls)
'''