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
                return None
            node.left, node.right = node.right, node.left
            flip(node.left)
            flip(node.right)
            return node
        
        return flip(root)
        '''
        let's say we wanna invert a tree who's root node is given
        swap node.left and node.right
        we need to do this recursively as we go down
        call the function on node.left and node.right
        stopping condition (return None) is when node doesn't exist (it's None)
        return root node (its tree is now flipped)
        '''