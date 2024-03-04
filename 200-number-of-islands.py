class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue

                queue = [(i,j)]
                while queue:
                    x,y = queue.pop(0)
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "-1"
                        queue += [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]
                count += 1
        
        return count




        
