def findMaxAverage(self, nums: list[int], k: int) -> float:
    i=0
    j=0
    sums = 0
    max_sum=float('-inf')
    while j<len(nums):
        sums = sums + nums[j]
        if (j-i+1) == k:
            max_sum = max(sums,max_sum)
            sums = sums - nums[i]
            i+=1
        j+=1
    return max_sum/k
