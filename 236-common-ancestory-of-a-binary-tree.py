# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative solution using a stack to run dfs on the tree and a dict to track parent-child relationships
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # create dict to track parents and child node relationships
        parent = {root: None}

        # create stack to run dfs on tree
        stack = [root]

        # run until p and q are found
        while p not in parent or q not in parent:

            # pop top of stack to operate on
            node = stack.pop()

            # search right
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

            # search left
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
        
        # p and q are found, so search backwards through parent to find common ancestor
        ancestors = set()

        # add all p ancestors
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # search q ancestors until common appears
        while q not in ancestors:
            q = parent[q]
        
        # q is common ancestor
        return q

# recursive solution using dfs to find p and q, then return common ancestor
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if root does not exist, return
        if not root:
            return None

        # if root is p or q, return root
        if root is p or root is q:
            return root

        # otherwise search left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right exist, this root is common ancestor
        if left and right:
            return root
        
        # pass down right or left, whichever one has the answer
        if left:
            return left
        else:
            return right
            