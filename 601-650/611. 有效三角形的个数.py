
class Solution:
    def triangleNumber(self, nums):
        num=0
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if 0 in dic:
            del dic[0]
        res = sorted(dic.items(), key=lambda x: x[0])
        nums=[a[0] for a in res]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if i==j and j==k and dic[nums[j]]>=3:
                        num+=self.gen_last_value(dic[nums[j]],3)
                    elif i==j  and j!=k and dic[nums[j]]>=2 and 2*nums[i]>nums[k]:
                        num += self.gen_last_value(dic[nums[j]],2)*dic[nums[k]]
                    elif j==k and i!=j and dic[nums[j]]>=2:
                        num += self.gen_last_value(dic[nums[j]], 2) * dic[nums[i]]
                    elif i!=j and j!=k and nums[i]+nums[j]>nums[k]:
                        num+=dic[nums[i]]*dic[nums[j]]*dic[nums[k]]
                    elif nums[i]+nums[j]<=nums[k]:
                        break
        return int(num)
    def gen_last_value(self,n, m):
        if n==m:
            return 1
        sum=1
        for i in range(n-m+1,n+1):
            sum*=i
        for i in range(1,m+1):
            sum/=i
        return sum


s=Solution()
print(s.gen_last_value(4,2))
test=[
{"input": [16,70,16,36,17,39,44,72,25,88,18,22,20,84,18,66,71,74,87,59,48,91,52,15,92,29,85,21,10,34,86,68,10,27,3,42,49,48,18,15,6,39,61,28,19,52,60,8,37,32,71,82,54,38,47,33,10,64,52,71,39,63,64,79,86,47,16,72,55,17,35,88,74,93,10,59,3,64,95,91,61,28,63,23,49,6,24,47,41,88,96,23,90,53,84,3,35,23,3,17]
, "output":75781},
{"input": [2,2,3,4], "output":3},
{"input": [0,1,0], "output":0},
]

for t in test:
    r=s.triangleNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.triangleNumber(t['input'])
