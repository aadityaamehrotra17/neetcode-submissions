# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge cases: both have 0 or 1 nodes
        # 0 -> true, 1 -> root.val == subroot.val
        # subroot is 0 -> true

        def isEqual(node1, node2):
            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            if node1 is None and node2 is None:
                return True
            if node1.val != node2.val:
                return False
            a = isEqual(node1.left, node2.left)
            b = isEqual(node1.right, node2.right)
            return a and b
            
        def traverse(node):
            if not node:
                return False
            if isEqual(node, subRoot):
                return True
            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)