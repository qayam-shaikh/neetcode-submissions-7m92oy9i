class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]