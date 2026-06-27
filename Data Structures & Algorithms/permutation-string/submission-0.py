class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=Counter(s1)
        k=len(s1)
        n=len(s2)
        curr=Counter(s2[:k])
        if curr==s: return True
        for r in range(k,n):
            curr[s2[r-k]]-=1
            if curr[s2[r-k]]==0:
                del curr[s2[r-k]]
            curr[s2[r]]+=1
            if curr==s: return True
        return False

