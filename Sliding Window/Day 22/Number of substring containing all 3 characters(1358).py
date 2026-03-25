class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i=0
        j=0
        res=0
        d=dict()
        n=len(s)
        while j<n:
            d[s[j]]=d.get(s[j],0)+1
            while len(d)==3:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
                res+= n-j
            j+=1
        return res
    

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i=0
        j=0
        res=0
        last_a=-1
        last_b=-1
        last_c=-1
        while j<len(s):
            if s[j] == 'a': last_a = j
            elif s[j] == 'b': last_b = j
            else: last_c = j

            if last_a != -1 and last_b != -1 and last_c != -1:
                res += 1 + min(last_a, last_b, last_c)
            j+=1
        return res