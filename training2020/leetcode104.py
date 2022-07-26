# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        global max_dep
        max_dep = 1
        def iter_tree(root, dep):
            global max_dep
            if root.left == None and root.right == None:
                if dep > max_dep:
                    max_dep = dep

            if root.left != None:
                iter_tree(root.left, dep+1)
            if root.right != None:
                iter_tree(root.right, dep+1)
        iter_tree(root, 1)
        return max_dep
