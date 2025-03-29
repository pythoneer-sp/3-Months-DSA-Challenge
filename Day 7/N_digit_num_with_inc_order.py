# Problem Statement: Given a number n, print all n-digit numbers in increasing order such that the digits in each number are strictly increasing from left to right. The output numbers should be printed in sorted order and each number should be printed in a separate line.


def increasingNumbers(n):
    res=[] #result array
    #Handling the case for n=1
    if n==1:
        res=[i for i in range(10)]
        return res
    #Array for containg digit
    arr=[]
    def solve(arr,res,n):
        #Base condition
        if n==0:
            ans=0
            for i in range(len(arr)):
                ans=ans*10+arr[i]
            res.append(ans)
            return
        #Handling large choices
        for i in range(1,10):
            # controlled recursion
            if len(arr)==0 or i>arr[-1]:
                arr.append(i)
                solve(arr,res,n-1)
                
                # backtrack
                arr.pop()
    solve(arr,res,n)
    return res

#Example
print(increasingNumbers(2))