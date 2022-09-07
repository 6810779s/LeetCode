# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            
            if not node.left and not node.right:
                return f"{node.val}"
            
            elif not node.right and node.left:
                l=dfs(node.left)
                return f"{node.val}({l})"
            
            
            elif not node.left and node.right:
                r=dfs(node.right)
                return f"{node.val}()({r})"
            
            else:
                l=dfs(node.left)
                r=dfs(node.right)
                return f"{node.val}({l})({r})"

        
        return dfs(root)