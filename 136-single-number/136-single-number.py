class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num=0
        for i in range(len(nums)):
            num=nums.pop(i)
            if num in nums:
                nums.insert(i,num)
            else:
                break
            
        return num
        
        