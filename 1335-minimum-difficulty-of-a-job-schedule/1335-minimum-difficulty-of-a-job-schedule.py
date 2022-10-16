class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        # Memoize maximum for every cut
        max_dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    max_dp[i][j] = jobDifficulty[i]
                else:
                    max_dp[i][j] = max(max_dp[i][j - 1], jobDifficulty[j])
        
        # Calculate minimum difficulty
        dp = [[0 for _ in range(n)] for _ in range(d)]
        for i in range(d):
            for j in range(i, min(n, n - d + i + 1)):
                if i == 0:
                    dp[i][j] = max_dp[i][j]
                else:
                    dp[i][j] = min(
                        dp[i - 1][k - 1] + max_dp[k][j]
                        for k in range(i, j + 1)
                    )
        return dp[d - 1][n - 1]