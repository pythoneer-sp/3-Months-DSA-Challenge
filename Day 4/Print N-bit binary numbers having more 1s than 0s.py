"""
Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.
Input:  
n = 2
Output: 
{"11", "10"}
Explanation: Valid numbers are those where each prefix has more 1s than 0s:
11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.
So, the output is "11, 10".
"""

def NBitBinary(n):
    # code here
    result=[]
    op=""
    one=0
    zero=0
    def solve(one,zero,n,op):
        if n==0:
            result.append(op)
            return
        op1=op+"1"
        solve(one+1,zero,n-1,op1)
        if one>zero:
            op2=op+"0"
            solve(one,zero+1,n-1,op2)
        return
    solve(one,zero,n,op)
    return result

print(NBitBinary(2))