class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        r,c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        def dfs(i,j):
            if (
                i<0 or j<0 or i>=r or j>=c or visited[i][j] or grid[i][j]!="1"
            ): return
            visited[i][j] = True
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        count = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j]=="1":
                    count += 1
                    dfs(i,j)
        return count