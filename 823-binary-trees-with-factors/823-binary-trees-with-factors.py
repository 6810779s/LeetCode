class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        dp={x:1 for x in arr}
        arr.sort()
        for i in range(len(arr)):
            
            for j in range(i):

                if arr[i]/arr[j] in dp:
                    dp[arr[i]]+=dp[arr[j]]*dp[arr[i]/arr[j]]
                    
        return sum(dp.values())%1000000007