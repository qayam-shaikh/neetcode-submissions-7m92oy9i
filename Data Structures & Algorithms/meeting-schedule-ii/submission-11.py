"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # heap solution
        if not intervals: return 0
        meetings=[(x.start,x.end) for x in intervals]
        meetings.sort(key=lambda x: x[0])
        heap=[meetings[0][1]]
        for start, end in meetings[1:]:
            if start < heap[0]:
                heapq.heappush(heap, end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
        return len(heap)
        