class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total&1: return False
        dp=[[False for _ in range(total+1)] for _ in range(len(nums))]
        def recurse(n,curr_sum):
            if n==len(nums): return False
            if curr_sum==0: return True
            if dp[n][curr_sum]: return dp[n][curr_sum]
            if nums[n]>curr_sum:
                return recurse(n+1,curr_sum)
            
            dp[n][curr_sum]= recurse(n+1,curr_sum-nums[n]) or recurse(n+1,curr_sum)
            return dp[n][curr_sum]
        return recurse(0,total//2)