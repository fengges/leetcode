class Solution:
    def nthUglyNumber(self, n):
        t=[0,0,0]
        result=[1]
        while n!=len(result):
            temp=[result[t[0]]*2,result[t[1]]*3,result[t[2]]*5]
            new=min(temp)
            result.append(new)
            for i,v in enumerate(temp):
                if v==new:
                    t[i]+=1
        return result[-1]