class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length<=1:
            return ""
        
        change = False
        for i in range(length//2):
            if palindrome[i]!="a":
                palindrome = palindrome[:i]+"a"+palindrome[i+1:]
                change=True
                break
        if not change:
            palindrome=palindrome[:length-1]+"b"
        return palindrome