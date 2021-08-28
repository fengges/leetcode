class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a=[ord(c)-ord('a') for c in firstWord]
        b=[ord(c)-ord('a') for c in secondWord]
        c=[ord(c)-ord('a') for c in targetWord]
        a=int(''.join([str(i) for i in a]))
        b=int(''.join([str(i) for i in b]))
        c=int(''.join([str(i) for i in c]))
        return a+b==c