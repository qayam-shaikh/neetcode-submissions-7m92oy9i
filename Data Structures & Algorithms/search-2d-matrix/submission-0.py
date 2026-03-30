class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            l, r = 0, n-1
            while l<= r:
                m = l + (r-l)//2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] > target:
                    r = m-1
                else:
                    l = m+1
        return False