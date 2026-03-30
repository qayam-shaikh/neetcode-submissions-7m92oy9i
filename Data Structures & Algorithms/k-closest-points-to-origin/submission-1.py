class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i,p in enumerate(points):
            ans.append((math.sqrt(p[0]**2 + p[1]**2), i))
        heapq.heapify(ans)
        res = []
        for _ in range(k):
            dist,idx = heapq.heappop(ans)
            res.append(points[idx])
        return res
        
