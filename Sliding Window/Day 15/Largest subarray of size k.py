def largest_subarray(arr, k):
    i=0
    j=0
    sums=0
    length=0
    while j<len(arr):
        sums+=arr[j]
        while sums>k:
            sums-=arr[i]
            i+=1
        if sums==k:
            length=max(length,j-i+1)
        j+=1
    return length

print(largest_subarray([2,3,1,4,2,3,5,1], 6))
