class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        ans = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + ans[p2]

                ans[p2] = total % 10
                ans[p1] += total // 10

        # Remove leading zeros
        i = 0
        while i < len(ans) - 1 and ans[i] == 0:
            i += 1

        return "".join(map(str, ans[i:]))