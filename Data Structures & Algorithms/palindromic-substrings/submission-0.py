class Solution:
    def countSubstrings(self, s: str) -> int:
        # explode around center idea of palindrome instead of bruteforce
        n=len(s)
        count=0
        for i in range(n):
            # odd centers
            left=right=i
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count
