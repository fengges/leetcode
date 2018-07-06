class Solution:
    def getPermutation(self, n, k):
        k-=1
        nums=[i for i in range(1,n+1)]
        sum=1
        fact=[]
        for i in range(1,n+1):
            sum*=i
            fact.append(sum)
        result=[]
        fact.reverse()
        lens=len(nums)
        for i in range(lens-1):
            n=int(k/fact[i+1])
            result.append(nums[n])
            del nums[n]
            k-=n*fact[i+1]

        result.extend(nums)
        r=[ str(i) for i in result]
        return "".join(r)








    def getPermutation1(self, n, k):
        nums=[i for i in range(1,n+1)]
        i=1
        while i!=k:
            nums=self.nextPermutation(nums)
            i+=1
        nums=[str(i) for i in nums]
        return ''.join(nums)

    def findIndex(self, nums):
        i = 0
        j = 0
        for j in range(len(nums) - 2, -1, -1):
            temp = nums[j + 1:]
            min = 100000000000000
            for t in temp:
                if t > nums[j] and t < min:
                    min = t
            try:
                i = temp.index(min)
            except:
                i = -1
            if i >= 0:
                i += j + 1
                return [i, j]
        return []


    def nextPermutation(self, nums):
        index = self.findIndex(nums)
        if len(index) == 2:
            i, j = index[0], index[1]
            nums[i], nums[j] = nums[j], nums[i]
            temp = nums[j + 1:]
            temp.sort()
            for t in range(len(temp)):
                nums[j + t + 1] = temp[t]
        else:
            nums.sort()
        return nums

s=Solution()
test=[
{"input": [3,1], "output": 213},



]

for t in test:
    r=s.getPermutation(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.getPermutation(t['input'][0], t['input'][1])