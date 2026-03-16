def MaximumSubarrayOfSizeK(arr, k):
    i=0
    j=0
    sums = 0
    max_sum= float('-inf')
    while j<len(arr):
        sums = sums + arr[j]
        if (j-i+1) == k:
            max_sum = max(sums,max_sum)
            sums = sums - arr[i]
            i+=1
        j+=1
    return max_sum