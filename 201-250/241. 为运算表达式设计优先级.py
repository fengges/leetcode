class Solution:
    def diffWaysToCompute(self, input):
        res=[]
        for i in range(len(input)):
            if input[i]=="+" or input[i]=="-" or input[i]=="*":
                left=self.diffWaysToCompute(input[0:i])
                right=self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i]=="+":
                            res.append(l+r)
                        elif input[i]=="-":
                            res.append(l-r)
                        else:
                            res.append(l*r)
        if len(res)==0:
            return [int(input)]
        return res
s=Solution()
test=[
{"input":  "2-1-1","output":[0, 2]},
{"input":  "2*3-4*5","output": [-34, -14, -10, -10, 10]},
]

for t in test:
    r=s.diffWaysToCompute(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))