class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        self.r = []
        self.find(root)
        return self.r

    def find(self, root):
        if root:
            if root.children:
                for t in root.children:
                    self.find(t)
            self.r.append(root.val)