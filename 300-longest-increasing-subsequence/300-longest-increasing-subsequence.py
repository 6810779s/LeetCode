class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=["false"]*len(nums)
        dp[0]=nums[0]
        idx=0
        for i in range(1,len(nums)):
            if nums[i]>dp[idx]:
                dp[idx+1]=nums[i]
                idx+=1
            else:
                l=0
                r=idx
                index=None
                while(l<=r):
                    mid=(r+l)//2
                    if dp[mid]>=nums[i]:
                        index=mid
                        r=mid-1
                    elif dp[mid]<nums[i]:
                        l=mid+1
                dp[index]=nums[i]
        result=0
        for i in dp:
            if i=="false":
                break
            else:
                result+=1
        return result