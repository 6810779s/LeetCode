class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        total=0
        
        while len(s)>1:
            if s[0] in dic:
                if s[0]+s[1] in dic:
                        total+=dic[s[0]+s[1]]
                        s=s[2:]
                else:
                    total+=dic[s[0]]
                    s=s[1:]
        
    
        if len(s)==1:
            total+=dic[s[0]]
        return total
            
                