"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res=[[root.val]]
        root=root.children
        queue=deque([root])
        
        while queue:
            
            node = queue.popleft()
            arr=[]
            node_arr=[]
            for i in node:
                arr.append(i.val)
                if i.children:
                    for j in i.children:
                        node_arr.append(j)
            if arr:
                res.append(arr)
            if node_arr:
                queue.append(node_arr)
   
        return res
        
         