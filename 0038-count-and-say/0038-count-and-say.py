class Solution:
    def countAndSay(self, n: int) -> str:    
        if n==1:
            return "1"

        string="1"
        
        for i in range(2,n+1):
            res=""
            num=""
            cnt=1
            for j in range(len(string)):
                if string[j]==num:
                    cnt+=1
                else:
                    if num:
                        res=res+str(cnt)+num
                        num=string[j]
                        cnt=1
                    else:
                        num=string[j]
            string=res+str(cnt)+num
        return string