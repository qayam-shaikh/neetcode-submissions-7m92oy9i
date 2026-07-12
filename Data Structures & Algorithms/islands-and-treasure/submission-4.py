class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        m,n=len(grid),len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        q=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            r,c =q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr>=m or nr<0 or nc>=n or nc<0 or grid[nr][nc]!=INF:continue
                grid[nr][nc]=grid[r][c]+1
                q.append((nr,nc))
            
