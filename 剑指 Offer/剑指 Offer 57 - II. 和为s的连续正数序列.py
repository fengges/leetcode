class Solution:
    def findContinuousSequence(self, target: int):
        result=[]
        for i in range(2,target//2+2):
            ans=target/i - (i-1)/2
            if ans==int(ans) and ans>0:
                ans=int(ans)
                result.append([ ans+t   for t in range(i)   ])
        result.reverse()
        return result
