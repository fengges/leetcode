from  util.tree import TreeNode,deserialize
class Solution(object):
    def sumNumbers(self, root):
        self.result=[]
        if root:
            self.find(root,0)
        return sum(self.result)
    def find(self,root,num):
        num=num*10+root.val
        if root.left is None and root.right is None:
            self.result.append(num)
        elif root.left is None:
            self.find(root.right,num)
        elif root.right is None:
            self.find(root.left,num)
        else:
            self.find(root.left, num)
            self.find(root.right, num)

s=Solution()

test=[
{"input":deserialize([1,2,3,None,5,None,None]),"output":25},
]
for t in test:
    r=s.sumNumbers(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.sumNumbers(t['input'])