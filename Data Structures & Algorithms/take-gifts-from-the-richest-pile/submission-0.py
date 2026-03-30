class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heap=heapq.heapify(gifts)
        for _ in range(k):
            val=-heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(val)))
        summ=0
        for x in gifts:
            summ=summ-x
        return summ
