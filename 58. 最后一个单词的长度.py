class Solution:
    def lengthOfLastWord(self, s):
        list=s.split(" ")
        list=[t for t in list if len(t)>0]
        if len(list)==0:
            return 0
        return len(list[-1])

s=Solution()

test=[
{"input":"","output":0},
{"input":"Hello World","output":5},
{"input":"a ","output":1},
]

for t in test:
    r=s.lengthOfLastWord(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.lengthOfLastWord(t['input'])
