from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        active_end=points[0][1]
        arrow=1
        for i in range(1,len(points)):
            start2=points[i][0]
            end2=points[i][1]
            if active_end>=start2:
                active_end=min(active_end,end2)
            else:
                arrow+=1
                active_end=end2
        return arrow