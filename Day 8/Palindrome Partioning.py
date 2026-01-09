"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

class Solution:
    def partition(self, s: str):
        def isPalindrome(st: str):
            start= 0
            end = len(st)-1
            while(start<end):
                if st[start]!=st[end]:
                    return False
                start += 1
                end -= 1
            return True
        def helper(s, temp, ind):
            if ind == len(s):
                ans.append(temp[:])
                return
            pal_string = ""
            for i in range(ind,len(s)):
                pal_string+=s[i]
                if isPalindrome(pal_string):
                    temp.append(pal_string)
                    helper(s,temp,i+1)
                    temp.pop()
                
        ans=[]
        temp=[]
        helper(s,temp,0)
        return ans
    