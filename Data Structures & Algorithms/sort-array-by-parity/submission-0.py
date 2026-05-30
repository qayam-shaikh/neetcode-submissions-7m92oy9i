class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        j=n-1
        ans=[-1]*n
        for num in nums:
            if num&1==0:
                ans[i]=num
                i+=1
            else:
                ans[j]=num
                j-=1
        return ans