class Solution:
    def nearestPalindromic(self, n):
        nums=[int(s) for s in n]
        for i in range(int(len(nums)/2)):
            if nums[i]!=nums[len(nums)-1-i]:
                nums[len(nums) - 1 - i]=nums[i]
        r=''.join([str(s) for s in nums])
        if r!=n:
            return r
        else:
            l=len(nums)
            if l%2==0:
                index=int(l/2)
                if nums[index]>0 and l!=2:
                    nums[index]=nums[index]-1
                    nums[index-1]=nums[index-1]-1
                else:
                    return '9'*(l-1)
            else:
                index=int(l/2)
                if nums[index]>0:
                    nums[index]=nums[index]-1
                elif l!=1:
                    return '9'*(l-1)
                else:
                    return str(nums[0]+1)
        return ''.join([str(s) for s in nums])

s=Solution()
test=[
{"input": '10', "output":'9'},
{"input": '11', "output":'9'},
{"input": '123', "output":'121'},
{"input": '1', "output":'0'},
]

for t in test:
    r=s.nearestPalindromic(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.nearestPalindromic(t['input'])