class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n=len(m)
        rot=n//2
        for r in range(rot):
            for c in range(r,n-r-1):
                m[r][c],m[c][n-r-1],m[n-r-1][n-c-1],m[n-c-1][r]=m[n-c-1][r],m[r][c],m[c][n-r-1],m[n-r-1][n-c-1]