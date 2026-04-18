class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = -1
        for c in s:
            if c=="1":
                ones+=1
        n=len(s)
        ans = ["0" for _ in range(n-1)]
        ans.append("1")
        i=0
        while ones:
            ans[i]="1"
            ones-=1
            i+=1
        return "".join(ans)
        

