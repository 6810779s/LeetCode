#[3,2,2]
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        
        dup=0
        original=0
        for i in range(len(nums)):
            if i+1 in dic and dic[i+1]==2:
                dup=i+1
            elif i+1 not in dic:
                original=i+1
            else:
                continue
        return [dup,original]
            
            
            
            
                
                