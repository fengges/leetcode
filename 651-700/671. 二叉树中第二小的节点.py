from util.tree import *
class Solution:
    def findSecondMinimumValue(self, root):
        if root ==None:
            return -1
        if root.left == None and root.right == None:
            return -1
        leftV =-1
        if root.left:
            if root.val == root.left.val:
                leftV =self.findSecondMinimumValue(root.left)
            else:
                leftV=root.left.val
        rightV = -1
        if root.right :
            if  root.val == root.right.val:
                rightV=self.findSecondMinimumValue(root.right)
            else:
                rightV = root.right.val
        if leftV != -1 and rightV != -1:
            return min(leftV, rightV)
        if leftV == -1:
            return rightV
        if rightV == -1:
            return leftV
        return -1

s=Solution()

test=[
{"input":  deserialize([2,2,5,None,None,5,7]),"output":10},
]

for t in test:
    r=s.findSecondMinimumValue(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
