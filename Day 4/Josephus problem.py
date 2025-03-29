# Find the winner of circular game ( Leetcode 1823 )

def findTheWinner( n: int, k: int) -> int:
    person=[]
    for i in range(1,n+1):
        person.append(i)
    k-=1
    out=0
    def solve(person,k,out):
        if len(person)==1:
            return
        out=(out+k)%len(person)
        person.pop(out)
        solve(person,k,out)
    solve(person,k,out)
    return person[0]


print(findTheWinner(40,7))