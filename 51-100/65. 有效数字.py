class Solution:
    def isNumber(self, s):
        # s=s.replace(" ","")
        nums=s.split("e")
        if len(nums)>2:
            return False
        elif len(nums)==2:
            try:
                a = int(nums[1])
                a = float(nums[0]+"1")
            except:
                return False

        try:
            a=float(nums[0])
        except:
            return False
        return True

s=Solution()

test=[
{"input":"96 e5","output":False},
{"input":"e9","output":False},
{"input":"6e6.5","output":False},
{"input":". 1","output":False},
{"input":"0","output":True},
{"input":" 0.1 ","output":True},
{"input":"abc","output":False},
{"input":"1 a","output":False},
{"input":"2e10","output":True},
{"input":"e","output":False},
]
for t in test:
    r=s.isNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isNumber(t['input'])

