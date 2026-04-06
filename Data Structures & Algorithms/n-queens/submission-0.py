class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board = [["."]*n for _ in range(n)]
        cols=set()
        d1=set()
        d2=set()

        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r-c in d1 or r+c in d2:
                    continue
                
                board[r][c]="Q"
                cols.add(c)
                d1.add(r-c)
                d2.add(r+c)

                backtrack(r+1)

                board[r][c]="."
                cols.remove(c)
                d1.remove(r-c)
                d2.remove(r+c)


        backtrack(0)
        return res