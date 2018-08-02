class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic={}
        for index,n in enumerate(nums):
            if n not in dic:
                dic[n]=[]
            dic[n].append(index)
        for n in dic:
            list=dic[n]
            for i in range(len(list)-1):
                if list[i+1]-list[i]<=k:
                    return True

        return False

s=Solution()
test=[

{"input": [[1,2,3,1],3], "output":True},
{"input": [[1,0,1,1],1], "output":True},
]

for t in test:
    r=s.containsNearbyDuplicate(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.containsNearbyDuplicate(t['input'][0], t['input'][1])