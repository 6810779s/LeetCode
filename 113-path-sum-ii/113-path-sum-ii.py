# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,arr):
            if not node:
                return
            
            if sum(arr+[node.val])==targetSum and not node.left and not node.right:
                res.append(arr+[node.val])
            
            dfs(node.left,arr+[node.val])
            dfs(node.right,arr+[node.val])
        
        dfs(root,[])
        return res