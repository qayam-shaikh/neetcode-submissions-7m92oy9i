class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        curr_start,curr_end=intervals[0]
        for start,end in intervals:
            if start<=curr_end:
                curr_end=max(curr_end,end)
            else:
                ans.append([curr_start,curr_end])
                curr_start=start
                curr_end=end
        ans.append([curr_start,curr_end])
        return ans