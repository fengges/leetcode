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