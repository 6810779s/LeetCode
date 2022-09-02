# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=deque([root])
        res=[]
        while queue:
            qlen = len(queue)
            num=0
            
            for i in range(qlen):
                node=queue.popleft()
                num+=node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            res.append(num/qlen)
        return res    
 