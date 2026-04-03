class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        def dfs(i, currxor):
            if i==len(nums):
                self.total += currxor
                return
            dfs(i+1, currxor^nums[i])
            dfs(i+1, currxor)
        dfs(0,0)
        return self.total