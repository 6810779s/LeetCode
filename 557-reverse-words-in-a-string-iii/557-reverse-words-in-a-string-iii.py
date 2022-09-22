class Solution:
    def reverseWords(self, s: str) -> str:
        word=''
        res=''
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                res=" "+word+res
                word=''
            else:
                print("s[i]!=' ' : ", s[i])
                word+=s[i]
        if word:
            res=word+res
        return res
            