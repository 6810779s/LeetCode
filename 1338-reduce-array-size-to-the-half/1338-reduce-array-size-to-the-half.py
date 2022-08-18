class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        n=len(arr)//2
        lst=sorted(count.values(),reverse=True)
        
        idx=0
        while n>0:
            n-=lst[idx]
            idx+=1
        return idx
        
        
        