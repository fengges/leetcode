class Solution:
    def smallestRangeI(self, A, K):
        tmp=max(A)-min(A)
        avg=1.0*sum(A)/len(A)
        for i in range(len(A)):
            if avg>A[i]:
                A[i]+=K
            elif avg==A[i]:
                print(A)
                print(K)
            else:
                A[i]-=K
        return min(max(A)-min(A),tmp)