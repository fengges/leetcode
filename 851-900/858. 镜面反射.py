class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """

        def gcd(m, n):
            while n != 0:
                m, n = n, m % n
            return m

        k = p * q // gcd(p, q)
        t1 = k // p
        t2 = k // q
        if t1 & 1 == 0:
            return 0
        if t2 & 1 == 0:
            return 2
        return 1
