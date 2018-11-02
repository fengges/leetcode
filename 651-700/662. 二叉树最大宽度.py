class Solution:
    def widthOfBinaryTree(self, root):
        r = []
        if root:
            root.val=1
            list = [root]
            next = 0
            start = 0
            level = []
            while len(list) > start:
                tmp = list[start]
                if tmp.left:
                    tmp.left.val=2*tmp.val
                    list.append(tmp.left)
                if tmp.right:
                    tmp.right.val = 2 * tmp.val+1
                    list.append(tmp.right)
                level.append(tmp.val)
                if next == start:
                    r.append(level)
                    next = len(list) - 1
                    level = []
                start += 1
        r=[t[-1]-t[0] for t in r]
        return max(r)+1