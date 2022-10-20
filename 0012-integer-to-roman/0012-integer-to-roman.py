class Solution:
    def intToRoman(self, num: int) -> str:
        number_arr = [["I","IV","V","IX"],["X","XL","L","XC"],["C","CD","D","CM"],["M"]]
        res=""
        idx = len(str(num))-1 
        
        while idx>=0:
            number = str(num)[idx]
            arr_idx = len(str(num))-idx-1 
            
            if number=="4":
                res = number_arr[arr_idx][1]+res
            elif number=="5":
                res = number_arr[arr_idx][2]+res
            elif number =="9":
                res = number_arr[arr_idx][3]+res
            elif number =="0":
                pass
            else:
                res = number_arr[arr_idx][0]+res
                num-=10**arr_idx
                if number !="1":
                    continue
            
            idx-=1
            
        return res
                
            
        
            
        
        
                
    
    
    
        
     