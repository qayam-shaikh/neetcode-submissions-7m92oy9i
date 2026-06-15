class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # optimal solution
        if not intervals: return [newInterval]
        ans=[]
        n=len(intervals)
        i=0
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        if i==n:
            return ans + [newInterval]
        cs,ce=newInterval
        while i<n and intervals[i][0]<=ce:
            cs=min(cs,intervals[i][0])
            ce=max(ce,intervals[i][1])
            i+=1
        ans.append([cs,ce])

        while i<n:
            ans.append(intervals[i])
            i+=1
        return ans