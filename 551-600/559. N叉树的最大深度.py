class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def maxDepth(self, root):
        if root:
            tmp=[self.maxDepth(n) for n in root.children ]
            tmp.append(0)
            return 1+max(tmp)
        return 0

