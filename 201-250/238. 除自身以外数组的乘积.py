class Solution:
    def productExceptSelf(self, nums):
        sum=1
        o=0
        for n in nums:
            if n==0:
                o+=1
                continue
            sum*=n
        if o>1:
            return [0 for i in nums]
        r=[]
        if o==1:
            for n in nums:
                if n==0:
                    r.append(sum)
                else:
                    r.append(0)
        else:
            for n in nums:
                r.append(int(sum/n))
        return r
