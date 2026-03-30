class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (
                ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9')
            )
        newStr = ''
        for c in s:
            if alphaNum(c):
                newStr += c.lower()
        return newStr == newStr[::-1]

        