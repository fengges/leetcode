class Solution:
    def maxDistToClosest(self, seats):
        index = []
        for ins, i in enumerate(seats):
            if i == 1:
                index.append(ins)
        maxL=0
        for i in range(len(index)-1):
            maxL=max(int((index[i+1]-index[i])/2),maxL)
        maxL=max(maxL,index[0])
        maxL=max(maxL,len(seats)-1-index[-1])
        return maxL

