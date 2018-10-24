import copy
class Solution:
    def combinationSum3(self, k, n):
        self.r=[]
        nums=[i+1 for i in range(9)]
        self.count(nums,k,n,0,[])
        if k==1 and n<=9:
            return [n]
        return self.r
    def count(self,nums,k,n,s,list):
        if k==2:
            left = s
            right =len(nums) - 1
            while left < right:
                all =  nums[left] + nums[right]
                if all > n:
                    right -= 1
                elif all< n:
                    left += 1
                else:
                    tmp=copy.deepcopy(list)
                    tmp.append(nums[left])
                    tmp.append( nums[right])
                    self.r.append(tmp)
                    left+=1
        else:
            for i in range(s,len(nums)-k+1):
                tmp_n=n-nums[i]
                if tmp_n<=0:
                    continue
                list.append(nums[i])
                self.count(nums,k-1,tmp_n,i+1,list)
                del list[-1]

s=Solution()

test=[
{"input": [6,30],"output":[]},
{"input": [3,7],"output":[]},
{"input": [2,18],"output":[]},

]

for t in test:
    r=s.combinationSum3(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.combinationSum3(t['input'][0],t['input'][1])