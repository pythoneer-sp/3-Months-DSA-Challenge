
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count=0
        active_end=intervals[0][1]
        for i in range(1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if active_end > start2:
                count+=1
                active_end=min(active_end,end2)
            else:
                active_end=end2
        return count
    


# Or,

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count=0
        active_end=intervals[0][0]
        for i,j in intervals:
            if i >= active_end:
                active_end=j
            else:
                count+=1
                active_end=min(active_end,j)
        return count