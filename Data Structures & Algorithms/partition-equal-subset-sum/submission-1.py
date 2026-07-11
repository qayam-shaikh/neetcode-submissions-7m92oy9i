class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total&1: return False
        def recurse(n,curr_sum):
            if n==0: return False
            if curr_sum==0: return True
            if nums[n-1]>curr_sum:
                return recurse(n-1,curr_sum)
            return recurse(n-1,curr_sum-nums[n-1]) or recurse(n-1,curr_sum)

        return recurse(len(nums),total//2)