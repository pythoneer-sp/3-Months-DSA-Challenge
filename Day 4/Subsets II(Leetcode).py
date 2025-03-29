# Leetcode 90 ~ Subsets II

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        op=[]
        result=[]
        def solve(nums,op):
            if len(nums)==0:
                result.append(op)
                return
            op1=op[:] 
            op2=op[:]
            op2.append(nums[0])
            nums=nums[1:]
            solve(nums,op1)
            solve(nums,op2)
        solve(nums,op)
        return list(map(list, set(map(tuple, result))))