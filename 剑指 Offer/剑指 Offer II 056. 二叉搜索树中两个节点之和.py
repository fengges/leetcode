class Solution:
    def findTarget(self, root, k):
        r=self.inorderTraversal(root)
        return self.twoSum(r,k)
    def twoSum(self, numbers, target):
        a=None
        for i in range(len(numbers)-1):
            if a==numbers[i]:
                continue
            a=numbers[i]
            b=None
            for j in range(i+1,len(numbers)):
                if b == numbers[j]:
                    continue
                b = numbers[j]
                if numbers[i]+numbers[j]==target:
                    return True
                elif   numbers[i]+numbers[j]>target:
                    break

        return  False
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