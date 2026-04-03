
from rpds import List



class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        visited=set()
        def get_next(index):
            return (index+nums[index])%n
        for i in range(n):
            if i in visited:
                continue
            slow=i
            fast=i
            while True:
                if slow in visited or fast in visited:
                    break
                next_slow=get_next(slow)
                next_fast=get_next(fast)
                next_next_fast=get_next(next_fast)

                if nums[slow] * nums[next_slow] <0 or slow == next_slow:
                    break
                
                if nums[fast] * nums[next_fast] <0 or fast == next_fast:
                    break
                
                if nums[next_fast] * nums[next_next_fast] <0 or next_fast == next_next_fast:
                    break

                slow=next_slow
                fast=next_next_fast

                if slow == fast:
                    return True

            curr = i
            val=nums[curr]
            while nums[curr] * val > 0:
                if curr in visited:
                    break
                visited.add(curr)
                curr = get_next(curr)
            
        return False