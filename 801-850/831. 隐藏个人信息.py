class Solution:
    def maskPII(self, S):
        index=S.find("@")
        if index<0:
            num=0
            for s in S:
                if s>="0" and s<="9":
                    num+=1

            t="***-***-"
            sum=0
            for s in S:
                if s >= "0" and s <= "9":
                    sum += 1
                    if num-sum<4:
                        t+=s
            if num>10:
                t="+"+'*'*(num-10)+'-'+t
            return t

        else:
            S=S.lower()
            list=S.split("@")
            return list[0][0]+"*****"+list[0][-1]+"@"+list[1]


s=Solution()
test=[
{"input": "+(501321)-50-23431", "output":"+***-***-***-3431"},
{"input": "LeetCode@LeetCode.com", "output":"l*****e@leetcode.com"},
{"input": "AB@qq.com", "output":"a*****b@qq.com"},
{"input":  "1(234)567-890", "output":"***-***-7890"},
{"input":  "86-(10)12345678", "output":"+**-***-***-5678"},
]

for t in test:
    r=s.maskPII(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maskPII(t['input'])