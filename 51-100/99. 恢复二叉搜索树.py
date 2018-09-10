from  util.tree import TreeNode,deserialize
import copy
class Solution:
    def recoverTree(self, root):
        list=self.inorderTraversal(root)
        list2=copy.deepcopy(sorted(list,key =lambda x:x.val))
        for i in range(len(list)):
            if list[i].val!=list2[i].val:
                list[i].val=list2[i].val
        return root

    def inorderTraversal(self, root):
        list = []
        result = []
        temp = root
        while len(list) > 0 or temp:
            while temp:
                list.append(temp)
                temp = temp.left
            if len(list) > 0:
                temp = list[-1]
                result.append(temp)
                temp = temp.right
                del list[-1]
        return result

s=Solution()

test=[
{"input":deserialize([1,3,None,None,2]),"output":True},
{"input":deserialize([3,1,4,None,None,2]),"output":True},


]


for t in test:
    r=s.recoverTree(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))