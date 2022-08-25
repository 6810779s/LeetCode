# from itertools import permutations
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_lst = list(magazine)
        for i in ransomNote:
            if i in m_lst:
                m_lst.remove(i)
            else:
                return False
        return True
        
#         lst=list(permutations(magazine,len(ransomNote)))
#         result=[]
#         for i in lst:
#             result.append(''.join(i))
        
#         print(result)
#         if ransomNote in result:
#             return True
#         return False
        