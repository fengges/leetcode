class BSTIterator(object):
    def __init__(self, root):
        self.que=[]
        self.bulid(root)
    def bulid(self,root):
        if root is None:
            return
        self.bulid(root.left)
        self.que.append(root.val)
        self.bulid(root.right)

    def hasNext(self):
        return len(self.que)!=0

    def next(self):
        r=self.que[0]
        del self.que[0]
        return r