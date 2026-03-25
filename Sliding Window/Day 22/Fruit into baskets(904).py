
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        j=0
        d=dict()
        while j<len(fruits):
            d[fruits[j]]=d.get(fruits[j],0)+1
            if len(d)>2: # instead of while we can also use if because we are only interested in the maximum length of the window and we will keep on increasing the window until we get more than 2 types of fruits
                d[fruits[i]]-=1
                if d[fruits[i]]==0:
                    del d[fruits[i]]
                i+=1
            j+=1
        return j-i # why not j-i+1 because we are increasing j at the end of the loop so it will be one step ahead of the last valid index of the window

"""
904. Fruit Into Baskets
This is a good example of a sliding window problem

Here i have used a different approach from previous ones

In previous we shrink the window until we get the requrired condition

But as we only want maximum length of the window we can just keep on increasing the window and if we get more than 2 types of fruits then we can shrink the window until we get 2 types of fruits
"""