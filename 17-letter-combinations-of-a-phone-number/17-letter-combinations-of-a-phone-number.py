class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0: return []
        dic={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        arr=[]    
        def dfs(string,idx):
            if len(string)==len(digits):
                arr.append(string)
                return
            for i in dic[int(digits[idx])]:
                dfs(string+i,idx+1)

        dfs("",0)
        return arr