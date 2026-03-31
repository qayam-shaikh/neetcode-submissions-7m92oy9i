class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        # heapq.heapify(minHeap)
        for ele in nums:
            heapq.heappush(minHeap, ele)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]            