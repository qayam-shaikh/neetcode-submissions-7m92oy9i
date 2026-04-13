class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            key = [0]*26
            for c in word:
                key[ord(c)-ord('a')]+=1
            key = tuple(key)
            if key not in ans:
                ans[key] = []
            ans[key].append(word)
        return list(ans.values())