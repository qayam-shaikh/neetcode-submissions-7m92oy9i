class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            ans += (n%2)*2**i
            n//=2
        return ans