from  util.tree import TreeNode,deserialize
class Solution:
    def inorderTraversal(self, root):
        list=[]
        result=[]
        temp=root
        while len(list)>0 or temp:
            while temp:
                list.append(temp)
                temp=temp.left
            if len(list)>0:
                temp=list[-1]
                result.append(temp.val)
                temp=temp.right
                del list[-1]
        return result
s=Solution()
test=[
{"input":deserialize([1,None,2,3]),"output":2},



]
for t in test:
    r=s.inorderTraversal(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.inorderTraversal(t['input'])




