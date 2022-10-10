class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        # if length==3:
        #     return sum(nums)
        nums.sort()
        total = nums[0]+nums[1]+nums[-1]
        
        for i in range(length-2):
            left = i+1
            right = length-1
            while left<right:
                    total_pointer = nums[i]+nums[left]+nums[right]
                    
                    if total_pointer > target : 
                        right -=1
                    elif total_pointer<target:
                        left+=1
                    else:
                        return total_pointer
                    
                    if abs(target - total_pointer)<abs(target - total):
                        total = total_pointer
                        
        return total
                    