from  util.tree import TreeNode,deserialize
class Solution:
    def findFrequentTreeSum(self, root):
        self.dic={}
        self.count(root)
        max=0
        for k in self.dic:
            if self.dic[k]>max:
                max=self.dic[k]
        r=[]
        for k in self.dic:
            if self.dic[k]==max:
                r.append(k)
        return r
    def count(self,root):
        if root is None:
            return 0
        sum=root.val+ self.count(root.left)+ self.count(root.right)
        if sum not in self.dic:
            self.dic[sum]=1
        else:
            self.dic[sum] += 1
        return sum



s=Solution()

test=[
{"input":deserialize([5,2,-3]),"output": [2, -3, 4]},
{"input":deserialize([5,2,-5]),"output": [2]},
]
for t in test:
    r=s.findFrequentTreeSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findFrequentTreeSum(t['input'])

