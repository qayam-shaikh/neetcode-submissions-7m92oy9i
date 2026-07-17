class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        arr=[0]*26
        for ch in s1:
            idx = ord(ch) - ord('a')
            arr[idx] += 1
        n=len(s2)
        if k>n: return False
        curr=[0]*26
        for r in range(k):
            idx = ord(s2[r])-ord('a')
            curr[idx]+=1
        if curr==arr: return True
        for r in range(k,n):
            curr[ord(s2[r-k])-ord('a')]-=1
            curr[ord(s2[r])-ord('a')]+=1
            if curr==arr: return True
        return False