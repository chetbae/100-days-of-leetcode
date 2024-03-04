class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        rots = []
        depth = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rots.append([(i,j+1),(i+1,j),(i,j-1),(i-1,j)])
        
        while any(rots):
            isEmpty = True
            for i in range(len(rots)):
                if rots[i]:
                    nextLayer = []
                    for x,y in rots[i]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            isEmpty = False
                            grid[x][y] = 2
                            nextLayer.extend([(x,y+1),(x+1,y),(x,y-1),(x-1,y)])
                    rots[i] = nextLayer
            if isEmpty:
                break
            
            depth += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return depth 