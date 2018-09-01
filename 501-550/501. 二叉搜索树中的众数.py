class Solution:
    def findMode(self, root):
        nums=self.inorderTraversal(root)
        dic={}
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        max=None
        r=[]
        for k in dic:
            if max is None or dic[k]>dic[max]:
                max=k
                r=[k]
            elif dic[k]==dic[max]:
                r.append(k)
        return r
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