"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # line sweep algo
        count=0
        start=[x.start for x in intervals]
        end=[x.end for x in intervals]
        start.sort()
        end.sort()
        end_ptr=0
        for s in start:
            if s<end[end_ptr]:
                count+=1
            else:
                end_ptr+=1
        return count

            