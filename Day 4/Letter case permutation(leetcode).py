# leetcode 784 ~ Letter case permutataion

"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""



def letterCasePermutation(s: str) -> list[str]:
    op=""   # created a empty string output
    result=[]   # created a empty list to store strings
    def solve(s,op):
        if len(s)==0:  # if the input becomes empty
            result.append(op)
            return
        if s[0].isalpha():   # if the string first letter is alphabet
            op1=op+s[0].lower()
            op2=op+s[0].upper()
            solve(s[1:],op1)
            solve(s[1:],op2)
        else:               # if the string first letter is numeric value
            solve(s[1:],op+s[0])
    solve(s,op)
    return result

print(letterCasePermutation("abc1"))