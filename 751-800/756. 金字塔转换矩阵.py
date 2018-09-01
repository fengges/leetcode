class Solution:
    def pyramidTransition(self, bottom, allowed):

        while len(bottom)>1:
            temp = ""
            for i in range(len(bottom)-1):
                index=self.find(allowed,bottom[i:i+2])
                if index==-1:
                    return False
                else:
                    temp += allowed[index][2]
                    del allowed[index]

            bottom=temp
        return True
    def find(self,allowed,t):
        for v,i in enumerate(allowed):
            if i.find(t)==0:
                return v
        return -1

s=Solution()

test=[
{"input": ["CB",["CDD","CBC","ACA","BDD","ADD","DCA","BAD","ADA"]], "output":True},
{"input": ["XXYX",["XXX", "XXY", "XYX", "XYY", "YXZ"]], "output":False},
{"input": ["XYZ",["XYD", "YZE", "DEA", "FFF"]], "output":True},
]

for t in test:
    r=s.pyramidTransition(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.pyramidTransition(t['input'][0], t['input'][1])

