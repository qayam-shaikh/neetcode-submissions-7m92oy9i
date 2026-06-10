class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mxp=mnp=ans=nums[0]
        for num in nums[1:]:
            cand = (num,mxp*num,mnp*num)
            mxp=max(cand)
            mnp=min(cand)
            ans=max(ans,mxp)
        return ans