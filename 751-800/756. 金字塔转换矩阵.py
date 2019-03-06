class Solution:
    def pyramidTransition(self, bottom, allowed):
        dic=set(allowed)
        return self.count(bottom,'',dic)
    def count(self,bottom,next,dic):
        if len(bottom)==1 and len(next)==1:
            return True
        if len(bottom)==1:
            return self.count(next,'',dic)
        for i in range(len(bottom) - 1):
            list = self.find(dic, bottom[i:i + 2])
            if len(list)==0:
                return False
            else:
                for l in list:
                    if self.count(bottom[1:],next+l[2],dic):
                        return True

                return False

    def find(self,dic,t):
        r=[]
        for k in dic:
            if k.find(t)==0:
                r.append(k)
        return r

s=Solution()

test=[
{"input": ["BCD",["ACC","ACB","ABD","DAA","BDC","BDB","DBC","BBD","BBC","DBD","BCC","CDD","ABA","BAB","DDC","CCD","DDA","CCA","DDD"]], "output":True},
{"input": ["CCC",["CBB","ACB","ABD","CDB","BDC","CBC","DBA","DBB","CAB","BCB","BCC","BAA","CCD","BDD","DDD","CCA","CAA","CCC","CCB"]], "output":True},
{"input": ["CB",["CDD","CBC","ACA","BDD","ADD","DCA","BAD","ADA"]], "output":True},
{"input": ["XXYX",["XXX", "XXY", "XYX", "XYY", "YXZ"]], "output":False},
{"input": ["XYZ",["XYD", "YZE", "DEA", "FFF"]], "output":True},
]
for t in test:
    r=s.pyramidTransition(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.pyramidTransition(t['input'][0], t['input'][1])

