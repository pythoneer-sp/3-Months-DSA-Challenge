from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        res=[]
        maxs=deque()
        while j<len(nums):
            while(len(maxs)>0 and maxs[-1]<nums[j]):
                maxs.pop()
            maxs.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1 == k:
                res.append(maxs[0])
                if maxs[0]==nums[i]:
                    maxs.popleft()
                i+=1
                j+=1

        return res