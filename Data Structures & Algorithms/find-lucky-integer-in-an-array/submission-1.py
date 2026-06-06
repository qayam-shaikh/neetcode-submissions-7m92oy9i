class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        ans=-1
        for key,value in freq.items():
            if key==value:
                ans=max(ans,key)
        return ans