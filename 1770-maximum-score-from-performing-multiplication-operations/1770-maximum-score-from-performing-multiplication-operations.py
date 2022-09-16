class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        prev = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            cur = [0] * (i + 2)
            for left in range(i, -1, -1):
                right = n + left - i - 1
                cur[left] = max(nums[left] * multipliers[i] + prev[left + 1],
                                nums[right] * multipliers[i] + prev[left])
                
                
            prev = cur
        
        return prev[0]
        
            