class Solution:
    def myAtoi(self, str):
        numStr=''
        o=True
        z=True
        for s in str:
            if s==' ' and o:
                continue
            elif (s=='-' or s=='+') and z:
                numStr += s
                o=False
                z=False
            elif s>='0' and s<='9' :
                numStr+=s
                o=False
                z=False
            else:
                break
        if len(numStr)==0:
            return 0
        try:
            num=int(numStr)
        except:
            return 0
        if num > 2147483647:
            return 2147483647
        elif num<-2147483648:
            return -2147483648
        else :
            return num


s=Solution()

test=[
{"input":"123-","output":123},
{"input":"-   234","output":0},
{"input":"-5-","output":-5},
{"input":"   +0 123","output":0},
{"input":"+1","output":1},
{"input":"-","output":0},
{"input":"42","output":42},
{"input":"   -42","output":-42},
{"input":"4193 with words","output":4193},
{"input":"words and 987","output":0},
{"input":"-91283472332","output":-2147483648},
      ]

for t in test:
    r=s.myAtoi(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.myAtoi(t['input'])
