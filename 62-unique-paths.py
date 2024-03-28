# backtracking solution storing all paths, memory limit exceeded
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # result array with all paths
        res = []

        # current path, initialize to empty
        path = [(0,0)]

        # backtrack to find all paths, starting at top left (0,0)
        self.dfs(0, 0, res, path, m, n)

        # return length of total paths
        return len(res)
    
    def dfs(self, i: int, j: int, res: List[List[List[int]]], path: List[List[int]], m: int, n: int) -> None:        
        # if reached target, add to res
        if i == m-1 and j == n-1:
            res.append(path)
            return
        
        # otherwise, go up and down if in bounds
        if i+1 < m:
            self.dfs(i+1, j, res, path+[(i+1,j)], m, n)
        if j+1 < n:
            self.dfs(i, j+1, res, path+[(i,j+1)], m, n)
    
# backtracking solution storing only count of paths, time limit exceeded
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # number of total paths
        res = [0]

        # backtrack to find all paths, starting at top left (0,0)
        self.dfs(0, 0, res, m, n)

        # return length of total paths
        return res[0]
    
    def dfs(self, i: int, j: int, res: int, m: int, n: int) -> None:      
        # if reached target, add to res
        if i == m-1 and j == n-1:
            res[0] += 1
            return
        
        # otherwise, go up and down if in bounds
        if i+1 < m:
            self.dfs(i+1, j, res, m, n)
        if j+1 < n:
            self.dfs(i, j+1, res, m, n)
    
# simplified backtracking, time limit exceeded
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(0, 0, m, n, 1)
    
    def dfs(self, i: int, j: int, m: int, n: int, steps: int) -> int:      
        # if reached target, add to res
        if steps == m+n-1:
            return 1
        
        # otherwise, go up and down if in bounds
        return (self.dfs(i+1, j, m, n, steps+1) if i+1 < m else 0) + (self.dfs(i, j+1, m, n, steps+1) if j+1 < n else 0)

# dp solution, O(m*n) time, O(m*n) space, beats 83.11%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp array, where dp[i][j] is the number of paths for i, j from 0,0 in an i x j grid
        # set dp[0][j] and dp[i][0] for 0 <= i < m, 0 <= j < n to 1 for base cases, e.g. only one way to go straight
        dp = [[1] * n for _ in range(m)]

        # start from 1 for the same reason as above, only 1 way to go in a straight line
        for i in range(1, m):
            for j in range(1, n):

                # dp[i][j] combines the number of paths from left and above
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# one row dp solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # one row dp solution
        # going straight right yields only one path, initialize base cases to 1
        dp = [1] * n

        # crunch numbers m-1 times, excluding once for initial base case row, i.e. range(1,m)
        for _ in range(m-1):
            
            # skip dp[0] as it stays 1 ~ going straight down also yields one path
            for i in range(1, n):
                dp[i] = dp[i-1] + dp[i]
                    
        return dp[-1]

# math solution, choosing from m-1 and n-1, combinatorics, tbh don't really get it (revise)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        j = 1

        for i in range(m+n-2, max(m,n)-1, -1):
            ans = ans * i // j
            j += 1
        
        return ans
