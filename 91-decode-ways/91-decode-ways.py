class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize = None)
        def helper(s):
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            ans = helper(s[1:])
            if s[1]!=0 and int(s[0:2]) <= 26:
                ans+=helper(s[2:])
            return ans
        
        return helper(s)