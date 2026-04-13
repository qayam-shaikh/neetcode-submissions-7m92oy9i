class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            key = [0]*26
            for c in word:
                key[ord(c)-ord('a')]+=1
            key = tuple(key)
            ans[key].append(word)
        return list(ans.values())