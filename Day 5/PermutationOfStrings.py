# Permutation of strings

# Given a string s. The task is to return a vector of string of all unique permutations of the given string, s that may contain duplicates in lexicographically sorted order. 

#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        op=""
        arr=[]
        def permute(s,op,arr):
            if len(s)==0:
                arr.append(op)
                return
            seen=set()
            for i in range(len(s)):
                if s[i] not in seen:
                    seen.add(s[i])
                    newIp=s[0:i]+s[i+1:]
                    newOp=op+s[i]
                    permute(newIp,newOp,arr)
            return arr
        permute(s,op,arr)
        return arr
        