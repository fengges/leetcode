class Solution:
    def sortArrayByParityII(self, A):
        a=[i for i in A if i%2==0]
        b= [i for i in A if i % 2 == 1]
        for i in range(len(a)):
            A[i*2]=a[i]
            A[i * 2+1] = b[i]
        return A