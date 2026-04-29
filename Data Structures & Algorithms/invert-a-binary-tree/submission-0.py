# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge cases: num of nodes = 0 or 1
        
        def flip(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            flip(node.right)
            flip(node.left)
            return node
        
        return flip(root)