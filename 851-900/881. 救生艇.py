class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        tmp=0
        l,r=0,len(people)-1
        while l<=r:
            if l==r:
                tmp+=1
                l+=1
            elif people[l]+people[r]<=limit:
                tmp+=1
                l+=1
                r-=1
            else:
                tmp+=1
                l+=1

        return tmp

s=Solution()
test=[
{"input": [[3,2,3,2,2],6], "output":3},
{"input": [[5,1,4,2],6], "output":2},
{"input": [[1,2],3], "output":1},
{"input": [[3,2,2,1],3], "output":3},
{"input": [[3,5,3,4],5], "output":4},
]

for t in test:
    r=s.numRescueBoats(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
