from collections import deque
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n= len(mat[0])
        x=m-1
        y=0
        while x!=0 or y!=n-1:
            copy_x = x
            copy_y = y
            result=[]
            while copy_x<=m-1 and copy_y<=n-1:
                result.append(mat[copy_x][copy_y])
                copy_x+=1
                copy_y+=1
            result.sort()
            copy_x = x
            copy_y = y
            for i in range(len(result)):
                mat[copy_x][copy_y]=result[i]
                copy_x+=1
                copy_y+=1
        
            if x==0:
                y+=1
                continue
            x-=1
        return mat
                