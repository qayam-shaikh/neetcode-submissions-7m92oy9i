class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cur = 1
        ans = [1 for _ in range(n)]
        for i in range(n):
            ans[i]*=cur
            cur*=nums[i]
        cur = 1
        for j in range(n-1,-1,-1):
            ans[j]*=cur
            cur*=nums[j]
        
        return ans

