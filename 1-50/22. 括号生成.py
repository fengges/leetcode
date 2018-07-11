class Solution:
    def generateParenthesis(self, n):
        num=2*n
        all={'(':1}
        t=[]
        for i in range(1,num):
            r={}
            for k in all:
                left=all[k]
                if left>0:
                    r[k+'('] = left + 1
                    r[k+')'] = left - 1
                else:
                    r[k+'(']=left+1
            all=r
        for k in all:
            if  r[k]==0:
                t.append(k)
        return t

s=Solution()

test=[
{"input": 3,"output":[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]},

      ]

for t in test:
    r=s.generateParenthesis(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.generateParenthesis(t['input'])