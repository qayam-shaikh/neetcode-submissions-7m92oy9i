class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        if len(s) == 1 or len(s)==0:
            return len(s)
        res = 1
        length = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in hashSet:
                    hashSet.clear()
                    res = max(res, length)
                    length = 0
                    break
                length += 1
                hashSet.add(s[j])
        return res
        