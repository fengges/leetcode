class Solution:
    def tree2str(self, t):
        if t is None:
            return ""
        left,right=self.tree2str(t.left),self.tree2str(t.right)
        if len(left)==0 and len(right)==0:
            return str(t.val)
        elif len(right)==0:
            return str(t.val)+"("+left+")"
        return str(t.val)+"("+left+")"+"("+right+")"