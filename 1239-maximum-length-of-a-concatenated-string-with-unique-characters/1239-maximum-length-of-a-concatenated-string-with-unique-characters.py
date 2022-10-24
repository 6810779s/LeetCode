class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        s_arr=[""]
        s_length=0
        for word in arr:
            for s in s_arr:
                string = word+s
                if len(string)==len(set(string)):
                    s_length=max(s_length,len(string))
                    s_arr.append(string)
        
        return s_length
                    
                