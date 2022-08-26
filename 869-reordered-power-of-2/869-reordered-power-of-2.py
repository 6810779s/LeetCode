from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n1=sorted(str(n))
        num=1
        cnt=0
        while len(str(num))<=len(n1):
            num_lst=sorted(str(num))
            if num_lst==n1:
                return True
            cnt+=1
            num=2**cnt
            
        return False
            
            
            
        
    
