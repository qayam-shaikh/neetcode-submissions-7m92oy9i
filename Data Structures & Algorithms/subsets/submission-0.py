class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if i==len(nums):
                res.append(subset)
                return
            # include nums[i]
            _subset = subset.copy()
            _subset.append(nums[i])
            dfs(i+1,_subset)
            # exclude nums[i]
            dfs(i+1,subset)
        dfs(0,[])
        return res