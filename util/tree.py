class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def deserialize(nums):
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