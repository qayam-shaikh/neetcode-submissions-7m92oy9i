class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        val = 1
        while val < n:
            val = val * 2
        return val == n