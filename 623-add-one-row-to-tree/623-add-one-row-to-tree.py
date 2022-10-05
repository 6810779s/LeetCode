# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        def dfs(root,cnt):
            if not root:
                return
            
            if cnt==depth-1:
                left = TreeNode(val,root.left,None)
                right = TreeNode(val,None,root.right)
                root.left = left
                root.right= right
                
                
            dfs(root.left,cnt+1)
            dfs(root.right,cnt+1)
            
            
        dfs(root,1)
        return root