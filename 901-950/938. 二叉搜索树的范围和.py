class Solution:
    def rangeSumBST(self, root, L, R):

        tmp=self.inorderTraversal(root)
        return sum(tmp[tmp.index(L):tmp.index(R)+1])
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