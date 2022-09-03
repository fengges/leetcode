# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        pop=[root]
        ans=[]
        while pop:
            t=pop.pop(0)
            ans.append(t.val)
            if t.left:
                pop.append(t.left)

            if t.right:
                pop.append(t.right)

        return ans