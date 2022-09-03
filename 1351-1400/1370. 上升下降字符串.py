class Solution:
    def sortString(self, s: str) -> str:
        ans=[0 for i in range(26)]
        for i in s:
            ans[ord(i)-ord('a')]+=1
        result=''
        while len(result)!=len(s):
            for i in range(26):
                if ans[i]!=0:
                    result+=chr(i+ord('a'))
                    ans[i]-=1

            for i in range(26):
                if ans[25-i]!=0:
                    result+=chr(25-i+ord('a'))
                    ans[25-i]-=1
        return result