class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            sums=0
            while n>0:
                digit=n%10
                sums+=digit**2
                n=n//10
            return sums
        slow=n
        fast=get_next(n)
        while fast != 1 and slow != fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast == 1

