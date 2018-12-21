class Solution:
    def findLongestChain(self, pairs):
        temp=sorted(pairs,key=lambda x:x[1])
        if len(temp)==0:
            return 0
        end=temp[0]
        r=1
        for t in range(1,len(temp)):
            if temp[t][0]>end[1]:
                end=temp[t]
                r+=1
        return r
