class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        summ = 0
        for i in range(m):
            for j in range(n):
                if i==j:
                    summ += mat[i][j]
                if i+j == m-1 and i!=j:
                    summ += mat[i][j]
        
        return summ