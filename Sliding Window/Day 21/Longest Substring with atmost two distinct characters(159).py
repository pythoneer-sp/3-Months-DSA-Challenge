def lengthOfLongestSubstring(s: str) -> int:
    # write your code here
    i=0
    j=0
    d=dict()
    res=0
    while j<len(s):
        d[s[j]]=d.get(s[j],0)+1
        while len(d)>2:
            d[s[i]]-=1
            if d[s[i]]==0:
                del d[s[i]]
            i+=1
        res=max(res,j-i+1)
        j+=1
    return res
