class Solution:
    def pancakeSort(self, arr)  :
        size=len(arr)

        ans=[]
        for i in range(size):
            t=size-i
            index=arr.index(t)
            if index==t-1:
                continue

            arr=arr[0:index+1][::-1]+arr[index+1:]
            arr=arr[0:t][::-1]+arr[t:]
            # print(arr)

            ans.extend([index+1,t])

        return ans

s=Solution()
null=None
test=[
    {"input":[3,2,4,1],"output":0},

]
for t in test:
    r=s.pancakeSort(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))