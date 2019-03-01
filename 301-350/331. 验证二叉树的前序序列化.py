class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

    def preOrderNonRec(self,Node):
        if Node == None:
            return
        # 用数组当栈
        stack = []
        while Node or stack:
            while Node:
                # 从根节点开始，一直找它的左子树
                print(Node.val)
                # 将右子树压入栈中
                stack.append(Node)
                # 一直往下找左子树
                Node = Node.left
            # while结束表示当前节点Node为空，即前一个节点没有左子树了
            # 栈中开始弹出上右子树，再重复前面步骤
            Node = stack.pop()
            Node = Node.right



s=Solution()

test=[
{"input":["123",6],"output": ["1+2+3", "1*2*3"] },
{"input":["105",5],"output": ["1+2+3", "1*2*3"] },

]
for t in test:
    r=s.addOperators(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))