class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRows = [0]*n
        for r in range(m-1,-1,-1):
            curRows = [0]*n
            curRows[n-1]=1
            for c in range(n-2,-1,-1):
                curRows[c]=curRows[c+1]+prevRows[c]
            prevRows = curRows
        return prevRows[0]
