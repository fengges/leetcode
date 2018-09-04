class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        r = []
        if root:
            list = [root]
            next = 0
            start = 0
            level = []
            while len(list) > start:
                tmp = list[start]
                if tmp.children:
                    for t in tmp.children:
                        list.append(t)
                level.append(tmp.val)
                if next == start:
                    r.append(level)
                    next = len(list) - 1
                    level = []
                start += 1
        return r