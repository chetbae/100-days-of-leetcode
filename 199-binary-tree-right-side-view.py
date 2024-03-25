# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return empty list if root is empty
        if not root:
            return []

        # run a DFS on the tree, adding only the rightmost node at each layer to the result
        ans = []

        # create queue
        queue = deque([root])
        
        # track width of each layer
        width = len(queue)
        i = 0

        # DFS as normal apart from tracking and adding rightmost node
        while queue:
            
            node = queue.popleft()

            # add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            # if end of layer, i.e. rightmost node, add to result and update width
            if i+1 == width:

                # add value to result
                ans.append(node.val)

                # update width
                width = len(queue)
                i = 0
            else:
                # otherwise update index
                i += 1
        
        return ans