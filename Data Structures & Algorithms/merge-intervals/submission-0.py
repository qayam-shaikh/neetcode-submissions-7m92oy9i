class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans=[]
        cs,ce=intervals[0]
        for s,e in intervals[1:]:
            if s<=ce:
                ce=max(ce,e)
            else:
                ans.append([cs,ce])
                cs=s
                ce=e
        ans.append([cs,ce])
        return ans