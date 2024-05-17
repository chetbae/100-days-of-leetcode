# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = [(root, targetSum-root.val, [root.val])]

        while stack:
            node, cost, path = stack.pop()

            if cost == 0 and not node.left and not node.right:
                ans.append(path)
            else:
                for child in [node.left, node.right]:
                    if child:
                        stack.append((child, cost-child.val, path + [child.val]))
        
        return ans