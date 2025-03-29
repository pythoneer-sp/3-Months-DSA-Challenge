def subsets(nums:list):
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
    return result


print(subsets([1,2,3]))