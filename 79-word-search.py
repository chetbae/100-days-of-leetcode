class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # get size of board and word
        m, n = len(board), len(board[0])
        
        # use dfs backtracking to search the board
        def dfs(row, col, word_i):
            
            # proceed if in bounds and current square is next letter
            if 0<=row<m and 0<=col<n and board[row][col] == word[word_i]:
                
                # if word index is last, then word has been found
                if word_i == len(word)-1:
                    return True
                    
                # mark square as visited
                temp, board[row][col] = board[row][col], '#'

                # search neighbouring squares
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:

                    # return True if path finds word
                    if dfs(row+i, col+j, word_i+1):
                        return True
                    
                # if no path from this square succeeds, unmark square
                board[row][col] = temp
                return False

            # otherwise backtrack
            else:
                return False

        # search each square
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
