class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for i in range(len(nums)-2):
            max_long=nums[i]
            length = nums[i+1]+nums[i+2]
            if max_long<length:
                return max_long+length
        
        return 0
        
            
        