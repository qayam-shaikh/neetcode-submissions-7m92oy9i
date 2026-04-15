class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = float('-inf')
        n=len(s)
        for c in range(ord('A'), ord('Z')+1):
            i,j,r = 0,0,0
            c = chr(c)
            while j<n:
                if s[j]==c:
                    j+=1
                elif r<k:
                    j+=1
                    r+=1
                elif s[i]==c:
                    i+=1
                else:
                    i+=1
                    r-=1
                ans = max(ans,j-i)
        return ans 