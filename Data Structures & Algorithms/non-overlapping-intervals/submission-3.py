class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals=0
        prev_end=intervals[0][1]
        for interval in intervals[1:]:
            start,end=interval
            if start<prev_end:
                prev_end=min(prev_end,end)
                removals+=1
            else:
                prev_end=end
        return removals