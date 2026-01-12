def moveZeroes(nums):
        zero_position=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[zero_position]=nums[zero_position],nums[i]
                zero_position+=1