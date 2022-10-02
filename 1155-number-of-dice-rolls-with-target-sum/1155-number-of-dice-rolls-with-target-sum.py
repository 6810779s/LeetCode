class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        
        memo = {}
        
        def dp(n, t):
            if (n,t) in memo:
                return memo[(n,t)]
            
            if n > t or n*k < t: return 0
            
            if n == 1: return 1
            
            ans = 0
            for i in range(1, k+1):
                ans += dp(n-1, t-i) % MOD
                
            memo[(n,t)] = ans%MOD
            return memo[(n,t)]
        
        return dp(n, target)