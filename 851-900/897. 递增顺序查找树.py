
class Solution:
    def increasingBST(self, root):
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
        for i in range(len(result)-1):
            result[i].left=None
            result[i].right =result[i+1]
        result[-1].left = None
        result[-1].right = None
        return result[0]