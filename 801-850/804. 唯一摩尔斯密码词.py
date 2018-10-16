class Solution:
    def uniqueMorseRepresentations(self, words):
        tmp=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic={}
        for word in words:
            s=""
            for w in word:
                s+=tmp[ord(w)-ord('a')]
            dic[s]=1
        return len(dic)

