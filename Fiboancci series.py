# Write a python program for fibonacci series using recurssion

n=int(input("Enter the term of series: "))
def fiboancci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fiboancci(n-2)+fiboancci(n-1)

for i in range(1,n+1):    
  print(fiboancci(i),end=" -> ")