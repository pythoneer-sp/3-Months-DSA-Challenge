def threeSum(nums):
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            s = i+1
            e = len(nums)-1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]
                if sum == 0:
                    res.append([nums[i],nums[s],nums[e]])
                    s+=1
                    e-=1
                    while s<e and nums[s] == nums[s-1]:
                        s+=1
                elif sum > 0:
                    e-=1
                else:
                    s+=1
        return res
        