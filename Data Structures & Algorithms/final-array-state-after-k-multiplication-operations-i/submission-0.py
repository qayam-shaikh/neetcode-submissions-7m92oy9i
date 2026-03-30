class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res=nums.copy()
        nums = [(x,i) for i,x in enumerate(nums)]
        heapq.heapify(nums)
        for _ in range(k):
            val,i=heapq.heappop(nums)
            heapq.heappush(nums,(multiplier*val,i))
            res[i] *= multiplier
        return res