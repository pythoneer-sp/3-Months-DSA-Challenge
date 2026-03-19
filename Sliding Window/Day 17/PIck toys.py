def pick_toys(toys, k):
    i=0
    j=0
    d=dict()
    max_toys=0
    while j<len(toys):
        d[toys[j]]=d.get(toys[j],0)+1
        while len(d)>k:
            d[toys[i]]-=1
            if d[toys[i]]==0:
                del d[toys[i]]
            i+=1
        max_toys=max(max_toys,j-i+1)
        j+=1
    return max_toys

print(pick_toys(['a','b','a','c','c','a','b'], 2))