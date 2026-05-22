class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        r,c=len(heights),len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,vis):
            vis.add((i,j))
            for dx,dy in directions:
                x,y=i+dx,j+dy
                if 0<=x<r and 0<=y<c:
                    if (x,y) not in vis and heights[x][y]>=heights[i][j]:
                        dfs(x,y,vis)
        pac,atl=set(),set()
        for j in range(c): dfs(0,j,pac)
        for i in range(r): dfs(i,0,pac)
        for j in range(c): dfs(r-1,j,atl)
        for i in range(r): dfs(i,c-1,atl)
        return list(pac&atl)