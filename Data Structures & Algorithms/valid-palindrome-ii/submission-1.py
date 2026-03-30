class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        newStr = '' 
        for i in range(len(s)):
            newStr = s[:i] + s[i+1:]
            if newStr == newStr[::-1]:
                return True
        return False