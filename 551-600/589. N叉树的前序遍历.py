class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        self.r = []
        self.find(root)
        return self.r

    def find(self, root):
        if root:
            self.r.append(root.val)
            if root.children:
                for t in root.children:
                    self.find(t)
