# Write a python program for checking number is prime or not using reccursion

num=int(input("Enter the number: "))
n=num-1
def primeOrNot(n):
    if n==1:  # Stopping condition
        return "Yes the number is prime"
    if num%n==0:
        return "No the number is not a prime"
    return primeOrNot(n-1)

print(primeOrNot(n))