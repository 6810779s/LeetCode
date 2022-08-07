class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=["a","e","i","o","u"]
        dic_cnt={"a":1,"e":1,"i":1,"o":1,"u":1}
        dic={"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"]}
        for i in range(1,n):
            dic_cnt_copy=dic_cnt.copy()
            dic_cnt["a"]=dic_cnt_copy["e"]+dic_cnt_copy["i"]+dic_cnt_copy["u"]
            dic_cnt["e"]=dic_cnt_copy["a"]+dic_cnt_copy["i"]
            dic_cnt["i"]=dic_cnt_copy["e"]+dic_cnt_copy["o"]
            dic_cnt["o"]=dic_cnt_copy["i"]
            dic_cnt["u"]=dic_cnt_copy["i"]+dic_cnt_copy["o"]
        return sum(dic_cnt.values())%(10**9 + 7)
    

        
#         def dfs(string,idx):
#             if len(string)==n:
#                 lst.append(string)
#                 return;
            
#             for i in arr:
#                 if len(string)==0:
#                     dfs(string+i,idx+1)
#                 else:
#                     if i in dic[string[idx-1]]:
#                         dfs(string+i,idx+1)
            
#         dfs("",0)
#         return len(lst)