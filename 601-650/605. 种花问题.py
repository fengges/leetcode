class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        index=[]
        for ins,i in enumerate(flowerbed):
            if i==1:
                index.append(ins)
        for i in range(len(index)-1):
            n-=int((index[i+1]-index[i]-2)/2)
        if len(index)!=0:
            n-=int(index[0]/2)
            n-=int((len(flowerbed)-index[-1]-1)/2)
        else:
            n-=int((len(flowerbed)+1)/2)
        if n<=0:
            return True
        else:
            return False

s=Solution()

test=[
{"input":[[1,0,0,0,1],1],"output":True},
{"input":[[1,0,0,0,1],2],"output":False},


]
for t in test:
    r=s.canPlaceFlowers(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.canPlaceFlowers(t['input'][0], t['input'][1])
