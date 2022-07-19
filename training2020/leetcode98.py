# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        global flag
        flag = True
        def iter_tree(node, left_max, right_min):
            global flag
            if flag == False:
                return
            if not node:
                return
            if left_max and node.val <= left_max:
                flag = False
                return
            if right_min and node.val >= right_min:
                flag = False
                return

            if node.left:
                if node.left.val >= node.val:
                    flag = False
                    return
                else:
                    iter_tree(node.left, left_max, node.val)
            if node.right:
                if node.right.val <= node.val:
                    flag = False
                    return
                else:
                    iter_tree(node.right, node.val, right_min)
        iter_tree(root, None, None)
        return flag

