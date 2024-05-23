# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # recursive func to preorder traverse the tree
        def searchSubtree(root):
            
            # mark empty children with a # token
            if not root:
                preorder.append("#")
            
            # otherwise append value and recurse
            else:
                preorder.append(str(root.val))
                searchSubtree(root.left)
                searchSubtree(root.right)
        
        preorder = []
        searchSubtree(root)

        out = ','.join(preorder)
        return out


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildSubtree(index):
            if index >= len(preorder) or preorder[index] == "#":
                return index+1, None
            
            node = TreeNode(int(preorder[index]))
            next_i, node.left = buildSubtree(index+1)
            next_i, node.right = buildSubtree(next_i)

            return next_i, node
            
        preorder = data.split(',')
        _, root = buildSubtree(0)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))