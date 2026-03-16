class Solution:

	
    def search(self,pat, txt):
        # code here
        i=0
        j=0
        k=len(pat)
        ans=0
        d=dict()
        for char in pat:
            d[char]=d.get(char,0)+1
        count=len(d)
        while j<len(txt):
            if txt[j] in pat:
                d[txt[j]]-=1
                if d[txt[j]]==0:
                    count-=1
            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                if count == 0:
                    ans+=1
                if txt[i] in pat:
                    d[txt[i]]+=1
                    if d[txt[i]]==1:
                        count+=1
                i+=1
                j+=1
        return ans