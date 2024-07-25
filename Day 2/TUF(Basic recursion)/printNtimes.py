# Write a program in python for printing any word N times using recursion

def printGfg(n):
        # Code here
        if n>0:
            printGfg(n-1)
            print("GFG", end=" ")

printGfg(10)