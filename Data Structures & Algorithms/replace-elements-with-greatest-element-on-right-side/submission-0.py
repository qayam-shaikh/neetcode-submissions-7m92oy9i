class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        mx = -1
        ans = [0]*n
        for j in range(n-1,-1,-1):
            ans[j]=mx
            mx=max(mx,arr[j])
        return ans