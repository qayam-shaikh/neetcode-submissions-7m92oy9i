class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31-1
        int_min = -2**31
        rev = 0
        while x:
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x-digit)//10
            if rev < int_min // 10 or rev > int_max // 10:
                return 0
            rev = rev * 10 + digit
        return rev