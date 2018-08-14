class Solution:
    def findShortestSubArray(self, nums):
        dic={}
        for i,n in enumerate(nums):
            if n not in dic:
                dic[n]=[]
            dic[n].append(i)
        maxList=[]
        maxL=0
        for k in dic:
            if len(dic[k])>maxL:
                maxL=len(dic[k])
                maxList=[dic[k]]
            elif len(dic[k])==maxL:
                maxList.append(dic[k])
        r=len(nums)
        for m in maxList:
            r=min(r,m[-1]-m[0]+1)
        return r


s = Solution()
test = [
{"input": [1,2,2,3,1], "output": 2},
{"input": [1,2,2,3,1,4,2], "output": 6},

]

for t in test:
    r = s.findShortestSubArray(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.findShortestSubArray(t['input'])