class Solution:
    def leafSimilar(self, root1, root2):
         list1=self.inorderTraversal(root1)
         list2=self.inorderTraversal(root2)
         if len(list1)!=len(list2):
             return False
         for i in range(len(list1)):
             if list1[i]!=list2[i]:
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
                if temp.left is None and temp.right is None:
                    result.append(temp.val)
                temp=temp.right
                del list[-1]
        return result