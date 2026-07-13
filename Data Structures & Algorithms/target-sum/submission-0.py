class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        dp=[[-1]*(2*total+1) for _ in range(n)]
        def findWays(i,s):
            if s==target and i==len(nums): return 1
            if i>=n: return 0
            if dp[i][s+total]!=-1: return dp[i][s+total]
            dp[i][s+total]=findWays(i+1,s+nums[i])+findWays(i+1,s-nums[i])
            return dp[i][s+total]
        return findWays(0,0)