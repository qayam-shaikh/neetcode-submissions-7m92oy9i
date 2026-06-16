"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        room=0
        max_room=0
        s=e=0
        start=[x.start for x in intervals]
        end=[x.end for x in intervals]
        
        start.sort()
        end.sort()

        while s<len(start) and e<len(end):
            if start[s]<end[e]:
                room+=1
                max_room=max(max_room,room)
                s+=1
            else:
                room-=1
                e+=1
        return max_room
