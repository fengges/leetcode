class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s0=max([len(a) for a in s.split('1')])
        s1=max([len(a) for a in s.split('0')])
        return s1>s0
