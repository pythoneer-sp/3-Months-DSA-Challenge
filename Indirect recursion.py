# Write a python program for printing n to 1 sequence
n=int( input("Enter the value of n: "))
def num(n):
    if n<=0:
        return
    print(n)
    num1(n-1)

def num1(n):
    print(n)
    num(n-1)

num(10)