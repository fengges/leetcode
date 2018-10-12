import functools
def cmp(a, b):
    if a%2==0:
        return -1
    return 1
class Solution:
    def sortArrayByParity(self, A):
        return sorted(A, key=functools.cmp_to_key(cmp))

