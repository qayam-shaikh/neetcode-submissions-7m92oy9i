class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        n=len(intervals)
        ans=[]
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
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