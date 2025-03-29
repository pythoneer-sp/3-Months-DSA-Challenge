# Leetcode problem (779)~ Kth symbol in grammar



def kthGrammar(n: int, k: int) -> int:
    if n==1 and k==1:
        return 0
    mid=(2**(n-1))//2
    if k<=mid:
        return kthGrammar(n-1,k)
    else:
        return 1-kthGrammar(n-1,k-mid)

