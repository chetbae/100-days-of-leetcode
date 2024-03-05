class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # number of rows and cols
        m, n = len(grid), len(grid[0])

        # queue of rotten oranges: '2'
        queue = deque()

        # track fresh oranges: '1'
        numFresh = 0
        
        # iterate through matrix, count num of fresh oranges and add rotten orange coords in queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        # elapsed time for BFS
        elapsed = 0

        # search until all rotten oranges are processed and no more fresh oranges
        while queue and numFresh > 0:
            
            # increment time
            elapsed += 1

            # process all oranges currently in queue
            for i in range(len(queue)):
                
                # pop current orange row and col
                x, y = queue.popleft()

                # process neighbours
                for nbx, nby in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:

                    # continue if neighbour is out of bounds
                    if nbx < 0 or nbx >= m or nby < 0 or nby >= n:
                        continue
                    
                    # continue if neighbour is empty or already visited (rotten):
                    if grid[nbx][nby] == 0 or grid[nbx][nby] == 2:
                        continue
                    
                    # otherwise mark neighbour as rotten, decrement fresh orange count, and add to queue
                    grid[nbx][nby] = 2
                    numFresh -= 1
                    queue.append((nbx,nby))

        # if there are still fresh oranges left, return -1
        if numFresh > 0:
            return -1
        
        # otherwise return elapsed time
        return elapsed