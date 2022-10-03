class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        stack = [['#', -1]] # store char, idx
        res = 0
        for i in range(len(colors)):
            if stack[-1][0] == colors[i]:
                res += min(neededTime[stack[-1][1]], neededTime[i])
                if neededTime[stack[-1][1]] < neededTime[i]:
                    stack[-1][1] = i   
            else:
                stack.append([colors[i], i])
        return res