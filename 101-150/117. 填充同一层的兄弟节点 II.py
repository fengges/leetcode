# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        list=self.levelOrder(root)
        for r in list:
            for j in range(len(r)-1):
                r[j].next=r[j+1]

    def levelOrder(self, root):
        r = []
        if root:
            list = [root]
            next = 0
            start = 0
            level = []
            while len(list) > start:
                tmp = list[start]
                if tmp.left:
                    list.append(tmp.left)
                if tmp.right:
                    list.append(tmp.right)
                level.append(tmp)
                if next == start:
                    r.append(level)
                    next = len(list) - 1
                    level = []
                start += 1
        return r