class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result=[]
        for i in words:
            letter=''
            for j in i:
                letter+=morse[ord(j)-97]
            if letter not in result:
                result.append(letter)
        
        return len(result)
        