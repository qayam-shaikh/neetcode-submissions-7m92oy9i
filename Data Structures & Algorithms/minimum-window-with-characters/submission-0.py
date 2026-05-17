class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        l = start = end = 0
        missing = len(t)

        for ch in t:
            need[ch] += 1
        
        for r, ch in enumerate(s):
            if need[ch]>0:
                missing -= 1
            need[ch] -= 1
            
            while missing == 0:
                if end == 0 or r-l+1 < end - start:
                    start, end = l, r+1
                need[s[l]] += 1
                if need[s[l]]>0:
                    missing += 1
                l += 1
        
        return s[start:end]