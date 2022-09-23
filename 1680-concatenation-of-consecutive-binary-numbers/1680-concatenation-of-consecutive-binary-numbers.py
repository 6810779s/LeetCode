class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary=''
        for i in range(1,n+1):
            binary+=bin(i)[2:]
        return int("0b"+binary,2)%((10**9)+7)
        
        
    
    