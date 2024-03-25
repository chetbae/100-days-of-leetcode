# spiral search O(m*n) time, O(m*n) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # create output array, set index to 0
        ans = [None] * (m * n)
        idx = 0

        # set direction to right initially (right-0, down-1, left-2, up-3)
        direction = 0

        # set current coord
        i, j = 0, 0

        # set upper and lower limits for each side
        left, top, right, bottom = 0, 0, 0, 0
        # spiral until all elements are checked
        while idx < m*n:

            # add current element to output array
            ans[idx] = matrix[i][j]
            idx += 1
            # decide which direction to go next
            match direction:
                
                # moving right
                case 0:
                    if j+1 < n-right:
                        j += 1
                    else:
                        direction = 1
                        i += 1
                        top += 1
                
                # moving down
                case 1:
                    if i+1 < m-bottom:
                        i += 1
                    else:
                        direction = 2
                        j -= 1
                        right += 1
                
                # moving left
                case 2:
                    if j-1 >= left:
                        j -= 1
                    else:
                        direction = 3
                        i -= 1
                        bottom += 1
                
                # moving up
                case 3:
                    if i-1 >= top:
                        i -= 1
                    else:
                        direction = 0
                        j += 1
                        left += 1
                
        return ans

# matrix rotate solution, O(m+n) time, O(1) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # output array
        ans = []

        # pop and rotate until matrix is empty
        while matrix:

            # add matrix row to output arr
            ans.extend(matrix.pop(0))

            # rotate matrix arraw counter clockwise by:
            # 1) reflect diagonally, 2) reverse row order
            matrix = [*zip(*matrix)][::-1]
        
        return ans