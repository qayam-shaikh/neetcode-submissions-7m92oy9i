class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]]==t[i]: continue
                return False
            if t[i] in hashmap.values():
                return False
            hashmap[s[i]]=t[i]
        return True