class Solution:
    def isValidBST(self, root):
        r=self.inorderTraversal(root)
        for i in range(len(r)-1):
            if r[i+1]<=r[i]:
                return False
        return True
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