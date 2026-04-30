class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])

        def change_row(row):
            for col in range(COL):
                if matrix[row][col] != 0:
                    matrix[row][col] = "X"
        
        def change_col(col):
            for row in range(ROW):
                if matrix[row][col] != 0:
                    matrix[row][col] = "X"

        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    change_row(i)
                    change_col(j)
        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0
        