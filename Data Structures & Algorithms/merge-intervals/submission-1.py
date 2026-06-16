class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        cs,ce=intervals[0]
        for interval in intervals[1:]:
            start,end = interval
            if start<=ce:
                ce=max(ce,end)
            else:
                ans.append([cs,ce])
                cs=start
                ce=end
        ans.append([cs,ce])
        return ans