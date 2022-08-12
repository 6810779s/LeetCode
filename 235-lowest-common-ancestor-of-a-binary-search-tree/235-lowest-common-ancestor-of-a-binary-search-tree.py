# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(node,n1,n2):
            if node==n1 or node==n2 or not node: return node
            
            left=rec(node.left,n1,n2)
            right=rec(node.right,n1,n2)
            
            if left and right: return node
            elif not left: return right
            elif not right: return left
            
            
            
        return rec(root,p,q)
        
        
        
        