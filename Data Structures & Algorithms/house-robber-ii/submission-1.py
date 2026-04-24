class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        mem1= [-1]*n
        mem2= [-1]*n
        if n==1: return nums[0]

        def dfs(i,end,mem):
            if i>=end+1: return 0
            if mem[i]!=-1: return mem[i]
            mem[i]=max(dfs(i+1,end,mem), nums[i]+dfs(i+2,end,mem))
            return mem[i]
        
        case1 = dfs(0,n-2,mem1)
        case2 = dfs(1,n-1,mem2)
        return max(case1, case2)