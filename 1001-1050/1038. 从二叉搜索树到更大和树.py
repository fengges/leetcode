class Solution:
    def bstToGst(self, root):
        def f(n):
            return f(n.right) + [n] + f(n.left) if n else []

        a = f(root)
        for i in range(1, len(a)):
            a[i].val += a[i - 1].val
        return root