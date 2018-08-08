class Solution:
    def topKFrequent(self, nums, k):
        dic={}
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        res=sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res=res[0:k]
        r=[]
        for re in res:
            r.append(re[0])
        return r

s = Solution()
test = [

    {"input": [[1,1,1,2,2,3],2], "output":[1,2]},
]

for t in test:
    r = s.topKFrequent(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.topKFrequent(t['input'][0], t['input'][1])
