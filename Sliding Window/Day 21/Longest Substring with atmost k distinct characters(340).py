def kDistinctChars(k, str):
    # Write your code here
    # Return an integer value
    i=0
    j=0
    d=dict()
    res=0
    while j<len(str):
        d[str[j]]=d.get(str[j],0)+1
        while len(d)>k:
            d[str[i]]-=1
            if d[str[i]]==0:
                del d[str[i]]
            i+=1
        res=max(res,j-i+1)
        j+=1
    return res