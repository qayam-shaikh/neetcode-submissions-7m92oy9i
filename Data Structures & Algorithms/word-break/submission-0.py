class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i:j+1] in wd and dp[j+1]:
                    dp[i]=True
                    break
        return dp[0]