class Solution:
    def largeGroupPositions(self, S):
        result=[]
        temp=None
        num=0
        start=-1
        end=-1
        for i,s in enumerate([a for a in S]):
            if temp==s:
                num+=1
                end=i
            else:
                temp=s
                if num>=3:
                    result.append([start,end])
                num=1
                start=i
        if num >= 3:
            result.append([start, end])
        return result

s=Solution()
test=[
{"input": "abcdddeeeeaabbbcd", "output":[[3,5],[6,9],[12,14]]},
{"input": "abc", "output":[]},
{"input": "abbxxxxzzz", "output":[[3,6]]},
]

for t in test:
    r=s.largeGroupPositions(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.largeGroupPositions(t['input'])