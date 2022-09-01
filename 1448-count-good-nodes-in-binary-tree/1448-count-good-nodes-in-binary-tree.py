# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(node,value):
            nonlocal res
            if not node:
                return
            
            value=max(node.val,value)
            if node.val>=value:
                res+=1
            
            dfs(node.left,value)
            dfs(node.right,value)
            
            
        dfs(root,-10001)
        return res