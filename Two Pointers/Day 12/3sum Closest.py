def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    res = float('inf')
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left<right:
            sums = nums[i]+nums[left]+nums[right]
            if abs(target-sums) < abs(target-res):
                res = sums
            if target == sums:
                return res
            elif target > sums:
                left +=1
            else:
                right -=1
    return res