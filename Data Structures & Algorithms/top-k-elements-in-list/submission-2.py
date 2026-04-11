class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (-count[num],-num))
        
        res = []
        for i in range(k):
            res.append(-heapq.heappop(heap)[1])
        return res