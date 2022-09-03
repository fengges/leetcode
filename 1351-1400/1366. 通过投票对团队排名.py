import functools

class Solution:
    def rankTeams(self, votes) -> str:


        size=len(votes[0])
        def cmp(a1,b1):
            a,b=a1[1],b1[1]
            for i in range(size):
                if a[i]==b[i]:
                    continue
                else:
                    return a[i]-b[i]
            return -ord(a1[0])+ord(b1[0])

        grid= [ [ 0  for i in range(size) ]  for j in enumerate(range(size))]

        dict={c:i for i,c in enumerate(votes[0])}
        for v in votes:
            for j,v in enumerate(v):
                index=dict[v]
                grid[index][j]+=1

        tmp=sorted([[votes[0][i],a] for i,a in enumerate(grid)],key=functools.cmp_to_key(cmp))
        tmp.reverse()
        tmp=[a[0] for a in tmp]
        return ''.join(tmp)
s=Solution()
null=None
test=[
    {"input":["BCA","CAB","CBA","ABC","ACB","BAC"],"output":'ABC'},
    {"input": ["WXYZ","XYZW"],"output":"XWYZ"},
    {"input":["ABC","ACB","ABC","ACB","ACB"],"output":'ACB'},


]
for t in test:
    r=s.rankTeams(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


