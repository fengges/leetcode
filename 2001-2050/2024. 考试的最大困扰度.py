class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.func(answerKey,k,'T'),self.func(answerKey,k,'F'))
    def func(self, answerKey: str, k: int,key) -> int:
        l=-1
        ans=0
        result=0
        for i,n in enumerate(answerKey):
            if n==key:
                while result>=k:
                    l+=1
                    if answerKey[l]==key:
                        result-=1
                result+=1
                ans=max(ans,i-l)
            else:
                ans=max(ans,i-l)
        return ans
