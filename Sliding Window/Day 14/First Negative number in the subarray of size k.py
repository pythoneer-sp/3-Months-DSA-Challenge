class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
         i=0
         j=0
         temp_list=[]
         result=[]
         while j<len(arr):
            if arr[j]<0:
                temp_list.append(arr[j])
            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                if len(temp_list) == 0:
                    result.append(0)
                else:
                    result.append(temp_list[0])
                    if arr[i] < 0:
                        temp_list.pop(0)
                j+=1
                i+=1
         return result
            