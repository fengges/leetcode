class Solution:
    def subsets(self, nums):
        ans=[]
        def fun(n,tmp):
            if not n:
                ans.append([t for t in tmp])
            else:
                fun(n[1:],[t for t in tmp])
                tmp.append(n[0])
                fun(n[1:],tmp)
                # tmp.pop()
        fun(nums,[])
        return ans

s=Solution()
test=[
    {"input":  [1,2,3],"output":[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]},

]

for t in test:
    r=s.subsets(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))