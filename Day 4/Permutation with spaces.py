

"""
Given a string s, you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in sorted increasing order of strings.
Input:
s = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Explanation:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".
"""

def permutation(s):
        # code here
        op=s[0]
        result=[]
        def solve(s,op):
            if len(s)==0:
                result.append(op)
                return
            op1=op + " " + s[0]
            op2=op + s[0]
            solve(s[1:],op1)
            solve(s[1:],op2)
        solve(s[1:],op)
        return result