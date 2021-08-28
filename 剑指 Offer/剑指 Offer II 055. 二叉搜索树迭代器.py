class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ans=[]
        def fun(node):
            if node:
                fun(node.left)
                self.ans.append(node.val)
                fun(node.right)
        fun(root)
        self.index=-1
    def next(self) -> int:
        self.index+=1
        return self.ans[self.index]

    def hasNext(self) -> bool:
        return self.index+1<len(self.ans)