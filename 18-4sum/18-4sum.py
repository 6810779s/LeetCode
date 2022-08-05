class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """  
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            # if nums[i]==nums[i-1]: continue
            for j in range(i+1,len(nums)-1):
                left=j+1
                right=len(nums)-1
                while left<right:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    arr=[nums[i],nums[j],nums[left],nums[right]]
                    if sum==target:
                        if arr not in result:
                            result.append(arr)
                        left+=1
                        right-=1

                    elif sum<target:
                        left+=1
                    else:
                        right-=1
                        
        
        return result
            
                
              
      
        