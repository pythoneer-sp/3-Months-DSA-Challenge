# Given a number k and string s of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of s at most k times.

#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        res = ["".join(s)]
        start=0
        def largestNum(s,k,res,start):
            if k==0 or start==len(s)-1: # base case
                return
            max_char = max(s[start:]) # find the maximum character from start to end
            for i in range (start+1,len(s)):
                if s[start]<s[i] and s[i]==max_char:
                    s[start],s[i]=s[i],s[start]
                    if "".join(s) > res[0]: # if the current number is greater than the previous number
                        res[0] = "".join(s)
                    largestNum(s,k-1,res,start+1) 
                    s[i],s[start]=s[start],s[i]  # backtrack
            largestNum(s,k,res,start+1) # recursive call for the number which is not swapped
        largestNum(list(s),k,res,start)
        return res[0]
