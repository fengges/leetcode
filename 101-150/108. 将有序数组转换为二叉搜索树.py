from  util.tree import TreeNode,deserialize

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        else:
            index=int(len(nums)/2)
            root=TreeNode(nums[index])
            root.left=self.sortedArrayToBST(nums[0:index])
            root.right=self.sortedArrayToBST(nums[index+1:])
            return root

s=Solution()

test=[
{"input":[-10,-3,0,5,9],"output":True},
{"input":["aabcc","dbbca","aadbbcbcac"],"output":True},


]


for t in test:
    r=s.sortedArrayToBST(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
