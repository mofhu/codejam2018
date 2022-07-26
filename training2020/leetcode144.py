# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        global out
        out = []
        def iter_tree(self, root: TreeNode):
            global out
            if root != None:
                out.append(root.val)
                iter_tree(self, root.left)
                iter_tree(self, root.right)
        iter_tree(self, root)
        return out


