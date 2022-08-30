class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        dic={}
        d=n-1
        for i in range(n):
            for j in range(n):
                dic[(j,d-i)]=matrix[j][d-i]
                
                if (i,j) in dic:
                    matrix[j][d-i]=dic[(i,j)]
                else:
                    matrix[j][d-i]=matrix[i][j]
        
        
                
            
            
            
            
            