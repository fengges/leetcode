class Solution:
    def validUtf8(self, data):
        size=len(data)
        if size<=0 or size>4:
            return False
        if size==1:
            return self.getBit(data[0])==0
        else:
            bit=self.getBit(data[0])
            if bit[size]==0 and sum(bit[0:size])==size:
                pass
            else:
                return False
            for i in range(1,size):
                bit=self.getBit(data[i])
                if bit[0]==1 and bit[1]==0:
                    continue
                else:
                    return False
        return True
    def getBit(self,num):
        r=[]
        for i in range(8):
            r.append(num%2)
            num>>=1
        r.reverse()
        return r

s=Solution()
test=[
{"input":[197,130,1], "output":True},

]

for t in test:
    r=s.validUtf8(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))