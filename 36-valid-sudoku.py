class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = [[set() for _ in range(3)] for _ in range(3)]
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                c = board[i][j]

                if c == ".":
                    continue

                if c in squares[i//3][j//3]:
                    return False
                else:
                    squares[i//3][j//3].add(c)
                
                if c in rows[i]:
                    return False
                else:
                    rows[i].add(c)
                
                if c in columns[j]:
                    return False
                else:
                    columns[j].add(c)
        
        return True