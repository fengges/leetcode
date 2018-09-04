deserialize
class Solution:
    def minDepth(self, root):
        self.result = []
        if root:
            self.find(root, 0)
        else:
            return 0
        return min(self.result)

    def find(self, root, num):
        num +=1
        if root.left is None and root.right is None:
            self.result.append(num)
        elif root.left is None:
            self.find(root.right, num)
        elif root.right is None:
            self.find(root.left, num)
        else:
            self.find(root.left, num)
            self.find(root.right, num)
