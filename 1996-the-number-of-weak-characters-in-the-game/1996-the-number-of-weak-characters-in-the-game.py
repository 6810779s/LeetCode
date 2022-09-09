class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        cnt=0
        
        max_properties=[properties[0][0],properties[0][1]]
        for i,j in properties:
            if max_properties[0]>i and max_properties[1]>j:
                cnt+=1
            else:
                max_properties[0]=i
                max_properties[1]=j
        return cnt
                
 