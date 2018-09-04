from  util.tree import TreeNode,deserialize
import copy
class Solution:
    def binaryTreePaths(self, root):
        self.result=[]
        if root:
            self.find(root,[])
            self.result=[ "->".join(r) for r in self.result]
        return self.result
    def find(self,root,num):
        num.append(str(root.val))
        if root.left is None and root.right is None:
            self.result.append(copy.deepcopy(num))
        elif root.left is None:
            self.find(root.right,num)
        elif root.right is None:
            self.find(root.left,num)
        else:
            self.find(root.left, num)
            self.find(root.right, num)
        del num[-1]


s=Solution()

test=[
{"input":deserialize([1,2,3,None,5]),"output": [2, -3, 4]},

]
for t in test:
    r=s.binaryTreePaths(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
