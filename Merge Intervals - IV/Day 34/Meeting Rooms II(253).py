class Solution:
    def minMeetingRooms(self, start, end):

        if not start:
            return 0
       
        start.sort()
        end.sort()
        
        first=0
        second=0
        
        current_rooms = 0
        max_rooms = 0
        
        while first < len(start):
            
            if start[first] < end[second]:
                current_rooms += 1
                first += 1
                
            else:
                current_rooms -= 1
                second += 1
                
            # Keep track of the highest number of rooms we ever needed at once
            max_rooms = max(max_rooms, current_rooms)
            
        return max_rooms
        