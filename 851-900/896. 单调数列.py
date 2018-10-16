class Solution:
    def isMonotonic(self, A):
        if len(A)<=2:
            return True
        des,aes=True,True
        for i in range(len(A)-1):
            if A[i+1]>A[i]:
                des=False
            if A[i+1]<A[i]:
                aes=False
        return des or aes

