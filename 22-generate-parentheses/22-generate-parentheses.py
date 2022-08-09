class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        
#         def checkSign(string):
#             openSign=0
#             closeSign=0
            
#             for i in string:
#                 if i=="(": openSign++
#                 else: closeSign++
            
#             if openSign==closeSign:
#                 return True
#             else:
#                 return False
            
        
        def dfs(sign,openSign,closeSign):
            if len(sign)==n*2 and openSign==closeSign:
                result.append(sign)
                return
            
            if openSign<=n:
                dfs(sign+"(",openSign+1,closeSign)
            if closeSign<openSign:
                dfs(sign+")",openSign,closeSign+1)
            
            
            
        dfs("",0,0)

        return result