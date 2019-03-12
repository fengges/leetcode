class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidSerialization(self, preorder):
        tmp=preorder.split(',')
        stack=[TreeNode(tmp[0])]
        start=1
        while start<len(tmp):
            if tmp[start]=='#':
                node=TreeNode(tmp[start])
                if self.add(stack,node)==False:
                    return False
            else:
                stack.append(TreeNode(tmp[start]))
            start += 1
        return len(stack)==1 and self.judge(stack[0])
    def judge(self,node):
        if node is None:
            return False
        if node.val=="#":
            return node.left is None and node.right is None
        return self.judge(node.left) and self.judge(node.right)
    def add(self,stack,node):
        if len(stack)==0:
            stack.append(node)
            return True
        t = stack.pop()
        if t.left is None:
            t.left = node
            stack.append(t)
            return True
        elif t.right is None:
            t.right = node
            return self.add(stack,t)
        else:
            return False


s=Solution()

test=[
{"input":"1,#,#,#,#","output":False },
{"input":"9,3,4,#,#,1,#,#,2,#,6,#,#","output":True },
{"input":"1","output":False },
]
for t in test:
    r=s.isValidSerialization(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))