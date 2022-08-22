class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        
        num = n
        while num>1:
            num/=4
            if num==1: return True
        return False
        