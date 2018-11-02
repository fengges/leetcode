from  util.tree import TreeNode,deserialize
class Solution:
    def convertBST(self, root):
        list=[]
        result=[]
        temp=root
        while len(list)>0 or temp:
            while temp:
                list.append(temp)
                temp=temp.left
            if len(list)>0:
                temp=list[-1]
                result.append(temp)
                temp=temp.right
                del list[-1]
        sum=0
        result.reverse()
        for node in result:
            sum+=node.val
            node.val=sum
        return root

s=Solution()

test=[
{"input":  deserialize([5,2,13]),"output":10},
]

for t in test:
    r=s.convertBST(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
