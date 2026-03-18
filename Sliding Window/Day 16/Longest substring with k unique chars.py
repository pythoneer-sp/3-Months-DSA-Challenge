class Solution:
    def longestKSubstr(self, s, k):
        # code here
        i=0
        j=0
        d=dict()
        length=-1
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            while len(d)>k:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            if len(d)==k:
                length=max(length,j-i+1)
            j+=1
        
        return length