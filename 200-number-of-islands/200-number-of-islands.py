class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0]) 
        cnt=0
        
        def dfs(x,y):
            if x>m-1 or x<0 or y>n-1 or y<0:
                return False
            
            if grid[x][y]=="1":
                grid[x][y]="0"
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
                return True
            return False
            
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j) is True:
                    cnt+=1
        
        return cnt
        