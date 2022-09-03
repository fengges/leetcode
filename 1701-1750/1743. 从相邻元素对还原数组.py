class Solution:
    def restoreArray(self, adjacentPairs) :
        arr=set()
        for a in adjacentPairs:
            arr.add(a[0])
            arr.add(a[1])
        arr=list(arr)
        dicts={v:i for i,v in enumerate(arr)}
        size=len(arr)
        dp=[[0 for i in range(size)] for j in range(size) ]
        flag=[True for i in range(size)]

        for a in adjacentPairs:
            dp[dicts[a[0]]][dicts[a[1]]]=1
            dp[dicts[a[1]]][dicts[a[0]]]=1

        def func(index,arr2):
            if size==len(arr2):
                return arr2
            for i,v in enumerate(dp[index]):
                if v==1 and flag[i]:
                    flag[i]=False
                    t=func(i,arr2+[arr[i]])
                    flag[i]=True
                    if t:
                        return t
            return None
        for i in range(size):
            flag[i]=False
            t=func(i,[arr[i]])
            if t:
                return t
            flag[i]=True

        return None

s=Solution()

test=[
    {"input": [[2,1],[3,4],[3,2]],"output":[1,2,3,4]},

]
for t in test:
    r=s.restoreArray(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))