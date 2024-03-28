# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # make map for value -> inorder index
        inorderMap = { value:index for index, value in enumerate(inorder) }

        # build subproblems from left and right subtrees
        def buildSubtree(inorder_lo, inorder_hi, preorder_root):
            
            # return empty child if no more nodes in subtree
            if inorder_lo > inorder_hi:
                return None

            # find root by indicated preorder index
            root = TreeNode(preorder[preorder_root])

            # find root value in inorder
            mid = inorderMap[root.val]
        
            # all nodes left of root in inorder traversal is in left, vice versa for right, we know preorder is current-left-right thus immediate right in preorder is left child root
            root.left = buildSubtree(inorder_lo, mid-1, preorder_root+1)
        
            # right child index in preorder = parent preorder index + length of left subtree + 1
            # since preorder is current-left-right, all left nodes are traversed before getting to the right
            # length of left subtree = inorder root position - inorder_lo
            root.right = buildSubtree(mid+1, inorder_hi, preorder_root + (mid - inorder_lo) + 1)

            return root

        # build binary tree
        return buildSubtree(0, len(preorder)-1, 0)




        
