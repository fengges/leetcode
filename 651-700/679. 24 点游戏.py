class Solution:
    def judgePoint24(self, cards) -> bool:

        if len(cards)==1:
            return cards[0]-24<abs(10e-10)
        size=len(cards)
        for i in range(size):
            for j in range(i+1,size):
                ans1=self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[i]+cards[j]])
                ans2=self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[i]-cards[j]])
                ans3=self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[j]-cards[i]])
                ans4=self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[i]*cards[j]])

                ans5=False if cards[j]==0 else self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[i]/cards[j]])
                ans6=False if cards[i]==0 else self.judgePoint24(cards[0:i]+cards[i+1:j]+cards[j+1:]+[cards[j]/cards[i]])
                if ans1 or ans2 or ans3 or ans4 or ans5 or ans6:
                    return True
        return False


s=Solution()

test=[

    {"input": [[1,2,1,2]],"output":2},
    {"input": [[3,3,8,8]],"output":2},

]
for t in test:
    r=s.judgePoint24(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
