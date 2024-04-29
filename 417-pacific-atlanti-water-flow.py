class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find the intersection of cells reachable from pacific and atlantic
        pacific = set()
        atlantic = set()
        m, n = len(heights), len(heights[0])
        visited = set()

        # dfs
        def search(i: int, j: int, prev: int, ocean: set):
            # stop if not in bounds or visited
            if not (0 <= i < m and 0 <= j < n) or (i,j) in visited:
                return

            height = heights[i][j]

            # stop if current is lesser than prev i.e. no flow
            if height >= prev:
                
                # if there is flow, add to set and search neighbours
                ocean.add((i,j))
                visited.add((i,j))

                for x, y in [(1,0), (0,1), (-1, 0), (0,-1)]:
                    search(i+y, j+x, height, ocean)
            
        # pacific
        for row in range(m):
            search(row, 0, -1, pacific)
        
        for col in range(1, n):
            search(0, col, -1, pacific)
        
        visited.clear()

        # atlantic
        for row in range(m):
            search(row, n-1, -1, atlantic)
        
        for col in range(n-1):
            search(m-1, col, -1, atlantic)

        # get intersection
        inter = pacific.intersection(atlantic)

        return [[a,b] for a,b in inter]