class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        length = 0
        if len(s)==1:
            return len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                length +=1
            else:
                return length
        