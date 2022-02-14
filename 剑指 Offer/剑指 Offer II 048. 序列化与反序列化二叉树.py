from  util.tree import TreeNode,deserialize
class Codec:
    def serialize(self, root):
        if root is None:
            return "[]"
        queen=[root]
        r=[]
        while len(queen)>0:
            temp=queen[0]
            del queen[0]
            if temp is None:
                r.append(None)
            else:
                r.append(temp.val)
                queen.append(temp.left)
                queen.append(temp.right)
        return str(r)

    def deserialize(self, data):

        nums=eval(data)
        if len(nums)==0:
            return None
        tree = [TreeNode(n) for n in nums]
        f = 0
        i = 1
        while i < len(tree):
            if tree[f].val is None:
                f += 1
                continue
            if tree[i].val is not None:
                tree[f].left = tree[i]
            else:
                tree[f].left = None
            i += 1
            if i == len(tree):
                break
            if tree[i].val is not None:
                tree[f].right = tree[i]
            else:
                tree[f].right = None
            i += 1
            f += 1
        return tree[0]

s=Codec()

test=[
    {"input":'[-1,0,1]',"output": [-1,0,1]},

]
for t in test:
    r=s.deserialize(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))