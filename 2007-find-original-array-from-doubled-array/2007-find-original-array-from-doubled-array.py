class Solution:
    def findOriginalArray(self, changed):
        cnt, ans = Counter(changed), []
        if len(changed) % 2: return []
        for x in sorted(cnt.keys()):
            if cnt[x] > cnt[x * 2]: return []
            # handle cases like [0,0,0,0]
            if x == 0:
                # similarly, odd length -> return []
                if cnt[x] % 2:
                    return []
                else: 
                    # add `0` `cnt[x] // 2` times 
                    ans += [0] * (cnt[x] // 2)
            else:
                # otherwise, we put the element `x` `cnt[x]` times to ans
                ans += [x] * cnt[x]
            cnt[2 * x] -= cnt[x]
        return ans