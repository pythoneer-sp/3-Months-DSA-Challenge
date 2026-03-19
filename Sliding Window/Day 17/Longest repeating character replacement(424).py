class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        d=dict()
        max_length=0
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            while ((j-i+1)-max(d.values())) > k: #Here we are checking through max for the dominant character
                d[s[i]]-=1
                i+=1
            max_length=max(max_length,j-i+1)
            j+=1
        return max_length
    
"""Another approach is to maintain the count of the most frequent character in the current window and check if the remaining characters are less than or equal to k. This way we can avoid calculating the maximum frequency in each iteration."""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        d=dict()
        max_length=0
        max_freq=0
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            max_freq=max(max_freq,d[s[j]]) #Here we are updating the max_freq for the dominant character
            while ((j-i+1)-max_freq) > k:
                d[s[i]]-=1
                i+=1
            max_length=max(max_length,j-i+1)
            j+=1
        return max_length