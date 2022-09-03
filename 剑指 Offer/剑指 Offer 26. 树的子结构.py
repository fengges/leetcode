# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if A is None or B is None:
            return False
        def dps(A,B):
            if A and B:
                return A.val==B.val and dps(A.left,B.left) and dps(A.right,B.right)
            else:
                if B is None:
                    return True
                else:
                    return False
        return dps(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)