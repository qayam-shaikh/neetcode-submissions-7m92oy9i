class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while x != 0:
            digit = int(x % 10)
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            if rev > INT_MAX // 10 or rev < INT_MIN // 10:
                return 0
            rev=rev*10+digit
        return rev









