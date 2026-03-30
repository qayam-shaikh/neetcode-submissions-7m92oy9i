class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>0:
            if len(stones)==1: break
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y>x:
                heapq.heappush(stones,x-y)
        return -stones[0] if len(stones) else 0
