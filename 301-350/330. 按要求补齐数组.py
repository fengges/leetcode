class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        L =len(nums)
        cnt=0
        i=0
        maxnum = 1
        while( maxnum<=n):
            if i<L and nums[i]<=maxnum:
                maxnum+=nums[i]
                i+=1
            else:
                maxnum<<=1
                cnt+=1
        return cnt
    def minPatches2(self, nums, n):
        tmp=set()
        tmp.add(0)
        for i in nums:
            self.add(tmp,i)
        r=0
        while True:
            index=self.find(tmp,n)
            if index>=0:
                r+=1
                self.add(tmp,index)
            else:
                break
        return r
    def find(self,dict,n):
        for i in range(n+1):
            if i not in dict:
                return i
        return -1

    def add(self,dict,num):
        tmp=[i+num for i in dict]
        for t in tmp:
            dict.add(t)

s=Solution()

test=[
{"input":[[1,2,31,33],2147483647],"output": 1 },
{"input":[[1,3],6],"output": 1 },
{"input":[[1,5,10],20],"output": 2 },
]
for t in test:
    r=s.minPatches(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))