
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1: return 0
        exit=[]
        idx=1
        
        while idx<=len(s):
            search=s[idx-1]
            if search not in s[idx:] and search not in exit:
                return idx-1
            else:
                exit.append(search)
            idx+=1   
        return -1
        
        
                
            