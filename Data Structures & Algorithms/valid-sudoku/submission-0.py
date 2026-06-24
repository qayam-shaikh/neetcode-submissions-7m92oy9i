class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b=board
        n=len(b)
        rows=[[False]*n for _ in range(n)]
        cols=[[False]*n for _ in range(n)]
        boxes=[[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if b[i][j]!=".":
                    num=ord(b[i][j])-ord('1')
                    boxInd=(i//3)*3+(j//3)
                    if rows[i][num] or cols[j][num] or boxes[boxInd][num]:
                        return False
                    rows[i][num]=cols[j][num]=boxes[boxInd][num]=True
        return True