class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = 0
        for a in s:
            sum1 ^= ord(a)
        sum2 = 0
        for a in t:
            sum2 ^= ord(a)
        return chr(sum2^sum1)