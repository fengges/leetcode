class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ans=[2**i for i in range(31)]
        ans=[''.join(sorted([i for i in str(a)])) for  a in ans]

        t=''.join(sorted([a for a in str(n)]))

        return t in ans