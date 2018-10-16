class Solution:
    def reverseOnlyLetters(self, S):
        l,r=0,len(S)-1
        tmp=[i for i in S]
        size=r+1
        while True:
            while l<size and not self.judge(S[l]):
                l+=1
            while r>=0 and not self.judge(S[r]):
                r-=1
            if l>=r:
                break
            tmp[l],tmp[r]=tmp[r],tmp[l]
            l+=1
            r-=1
        return ''.join(tmp)

    def judge(self,s):
        if (ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z')):
            return True
        else:
            return False

s=Solution()

test=[
{"input":"7_28]","output":"7_28]"},
{"input":"ab-cd","output":"dc-ba"},
{"input":"a-bC-dEf-ghIj","output":"j-Ih-gfE-dCba"},
{"input":"Test1ng-Leet=code-Q!","output":"Qedo1ct-eeLg=ntse-T!"},
]
for t in test:
    r=s.reverseOnlyLetters(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))