class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefSum=[0]*(n+1)
        for i in range(n):
            prefSum[i+1]=prefSum[i]+nums[i]
        count=defaultdict(int)
        count[0]=1
        ans=0
        for i in range(n):
            need=prefSum[i+1]-k
            ans+=count[need]
            count[prefSum[i+1]]+=1
        return ans
