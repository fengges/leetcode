class Solution:
    def findKthNumber(self, m, n, k):
        if k==1:
            return 1
        m1,n1=1,1
        s=1
        while m1<m or n1<n:
            a1=(m1+1)*n1
            a2=m1*(n1+1)
            if (m1<m and a1<a2) or n1==n:
                tmp=a1
                m1+=1
            else:
                tmp = a2
                n1+=1
            s+=1
            if s==k:
                return tmp

s = Solution()
test = [
    {"input":[3,3,5], "output": 5},
]

for t in test:
    r = s.findKthNumber(t['input'][0],t['input'][1],t['input'][2])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))