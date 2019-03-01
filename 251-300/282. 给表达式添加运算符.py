class Solution:
    def addOperators(self,num,target):
        res=[]
        self.addOperatorsDFS(num, target, 0, 0, "", res)
        return res
    def addOperatorsDFS(self,num,target, diff, curNum,out, res):
        if len(num) == 0 and curNum == target:
            res.append(out)
        for i in range(1,len(num)+1):
            cur = num[0:i]
            if len(cur) > 1 and cur[0] == '0':
                return
            next = num[i:]
            if len(out) > 0:
                self.addOperatorsDFS(next, target, int(cur), curNum + int(cur), out + "+" + cur, res)
                self.addOperatorsDFS(next, target, -int(cur), curNum - int(cur), out + "-" + cur, res)
                self.addOperatorsDFS(next, target, diff * int(cur), (curNum - diff) + diff * int(cur), out + "*" + cur, res)
            else:
                self.addOperatorsDFS(next, target, int(cur), int(cur), cur, res)

s=Solution()

test=[
{"input":["123",6],"output": ["1+2+3", "1*2*3"] },
{"input":["105",5],"output": ["1+2+3", "1*2*3"] },

]
for t in test:
    r=s.addOperators(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

