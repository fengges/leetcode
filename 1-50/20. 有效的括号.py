class Solution:
    def isValid(self, s):
        # isin=['(','[','{']
        out=[')',']','}']
        dic={')':'(',']':'[','}':'{'}
        isF=True
        list=[]
        for i in s:
            if i in out:
                if len(list)>0 and dic[i]==list[-1] :
                    del list[-1]
                else:
                    isF=False
            else:
                list.append(i)
        if len(list)!=0:
            isF=False
        return isF

s=Solution()

test=[
{"input": "[","output":False},
{"input": "","output":True},
{"input": "]","output":False},
{"input": "()","output":True},
{"input": "()[]{}","output":True},
{"input": "(]","output":False},
{"input":"([)]","output":False},
{"input":"{[]}","output":True},
      ]

for t in test:
    r=s.isValid(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isValid(t['input'])