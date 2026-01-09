def twoSum(numbers, target: int):
    l = 0
    r = len(numbers)- 1
    i = []
    while l <= r:
        if numbers[l] + numbers[r] == target:
            i.append(l+1)
            i.append(r+1)
            return i
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l+=1