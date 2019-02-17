class Solution:
    def sumEvenAfterQueries(self, A, queries):
        r=[]
        all=sum([a for a in A if a%2==0])
        for q in queries:
            tmp=A[q[1]]
            if tmp%2==0:
                all-=tmp
            tmp+=q[0]
            if tmp%2==0:
                all+=tmp
            A[q[1]]=tmp
            r.append(all)
        return r
