# Write a program in python for printing 1 to N natural number using recursion

def printNos(N):
    if N>0:
        printNos(N-1)
        print(N,end=" ")


printNos(10)