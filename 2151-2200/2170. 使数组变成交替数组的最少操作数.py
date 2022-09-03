import collections
class Solution:
    def minimumOperations(self, nums) -> int:
        if len(nums)==1: return 0
        ans1,ans2=nums[::2],nums[1::2]
        dic1,dic2=collections.Counter(ans1),collections.Counter(ans2)
        item1,item2=max(dic1.items(),key=lambda x:x[1]),max(dic2.items(),key=lambda x:x[1])
        size1,size2=len(ans1),len(ans2)
        if item1[0]==item2[0]:
            a,b=size1-item1[1],size2-item2[1]

            dic2.pop(item2[0])
            if dic2:
                item2=max(dic2.items(),key=lambda x:x[1])
            else:
                item2=[1,0]
            c=a+size2-item2[1]

            dic1.pop(item1[0])
            if dic1:
                item1=max(dic1.items(),key=lambda x:x[1])
            else:
                item1=[1,0]
            d=size1-item1[1]+b
            return min(c,d)

        else:
            return size1-item1[1]+size2-item2[1]
s=Solution()

test=[
    {"input":[1,2,2,2,2],"output":2},

]
for t in test:
    r=s.minimumOperations(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))