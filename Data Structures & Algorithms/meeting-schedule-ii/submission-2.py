class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        s,e,rooms,max_rooms=0,0,0,0
        while s < len(start_times):
            if start_times[s] < end_times[e]:
                rooms+=1
                s+=1
            else:
                rooms -=1
                e+=1
            max_rooms = max(max_rooms,rooms)
        return max_rooms