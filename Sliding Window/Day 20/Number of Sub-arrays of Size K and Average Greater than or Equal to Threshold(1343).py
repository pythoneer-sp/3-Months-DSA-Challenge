
from rpds import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i=0
        j=0
        sum=0
        res=0
        while j<len(arr):
            sum += arr[j]
            if j-i+1 == k:
                if sum/k >= threshold:
                    res+=1
                sum= sum - arr[i]
                i+=1
            j+=1
        return res