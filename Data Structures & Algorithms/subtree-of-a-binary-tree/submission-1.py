# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def isEqual(n1, n2):
            if not n1 and not n2:
                return True
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            return isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)

        def traverseCheck(node):
            if not node:
                return None
            if isEqual(node, subRoot):
                nonlocal res
                res = True
            traverseCheck(node.left)
            traverseCheck(node.right)

        traverseCheck(root)
        return res