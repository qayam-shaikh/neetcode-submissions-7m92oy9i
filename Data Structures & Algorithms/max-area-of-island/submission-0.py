class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0 or visited[r][c]:
                return 0
            visited[r][c]=True
            a1=dfs(r+1,c)
            a2=dfs(r-1,c)
            a3=dfs(r,c+1)
            a4=dfs(r,c-1)
            return 1+a1+a2+a3+a4
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c]==1:
                    area=dfs(r,c)
                    maxArea=max(maxArea,area)
        return maxArea
