class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        hashSet = set()
        res = 0
        while r<len(s):
            if s[r] in hashSet:
                res = max(res, r-l)
                while s[l]!=s[r]:
                    hashSet.remove(s[l])
                    l+=1
                l+=1
            hashSet.add(s[r])
            res = max(res, r-l+1)
            r+=1
            
        return res
