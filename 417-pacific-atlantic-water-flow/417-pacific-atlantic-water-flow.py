class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        
        
        pacific_Ocean=[]
        atlantic_Ocean=[]
        
        p_set=set()
        a_set=set()
        for i in range(m):
            pacific_Ocean.append((i,0))
            atlantic_Ocean.append((i,n-1))
        
        for i in range(n):
            pacific_Ocean.append((0,i))
            atlantic_Ocean.append((m-1,i))
        
        
        def bothOcean(x,y,set_o):
            set_o.add((x,y))
            d=[(1,0),(-1,0),(0,1),(0,-1)]
            
            for i,j in d:
                x_new,y_new=x+i,y+j
                
                if 0<=x_new<m and 0<=y_new<n and (x_new,y_new) not in set_o and heights[x][y]<=heights[x_new][y_new]:
                    
                    bothOcean(x_new,y_new,set_o)
                
        
        for (i,j) in pacific_Ocean:
            bothOcean(i,j,p_set)
        
        for (i,j) in atlantic_Ocean:
            bothOcean(i,j,a_set)
        
        return p_set&a_set
                
        