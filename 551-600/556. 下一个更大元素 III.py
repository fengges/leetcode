class Solution(object):
    def nextGreaterElement(self, n):
        nums=[int(s) for s in str(n)]
        t=self.nextPermutation(nums)
        n=int(''.join([str(i) for i in t]))
        if n<-2147483648 or n>2147483647:
            return -1
        return n
    def findIndex(self,nums):
        i=0
        j=0
        for j in range(len(nums)-2,-1,-1):
            temp=nums[j+1:]
            min=100000000000000
            for t in temp:
                if t>nums[j] and t<min:
                    min=t
            try:
                i=temp.index(min)
            except:
                i=-1
            if i>=0:
                i+=j+1
                return [i,j]
        return []
    def nextPermutation(self, nums):

        index=self.findIndex(nums)
        if len(index)==2:
            i, j = index[0], index[1]
            nums[i],nums[j]=nums[j],nums[i]
            temp=nums[j+1:]
            temp.sort()
            for t in range(len(temp)):
                nums[j+t+1]=temp[t]
            return nums
        else:
            return [-1]
