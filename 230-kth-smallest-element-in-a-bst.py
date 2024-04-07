# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        # inorder traversal
        while stack or root:

            # add left nodes onto the stack
            while root:
                stack.append(root)
                root = root.left
            
            # leftmost node, run operation and check right
            root = stack.pop()

            # if k is 1, this is the kth node
            if k == 1:
                return root.val
            # otherwise decrement
            k -= 1

            root = root.right
        
        
            
