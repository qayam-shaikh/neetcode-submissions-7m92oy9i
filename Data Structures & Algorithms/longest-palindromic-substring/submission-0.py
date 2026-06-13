class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=0
        max_len=1
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                cur_len=right-left+1
                if cur_len>max_len:
                    max_len=cur_len
                    start=left
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                cur_len=right-left+1
                if cur_len>max_len:
                    max_len=cur_len
                    start=left
                left-=1
                right+=1
        return s[start:start+max_len]