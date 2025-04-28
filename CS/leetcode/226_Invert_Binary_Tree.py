# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        rtype = root
        # recursive call swap right and left child substree
        if root is None:
            return
        tmp = root.left
        root.left = root.right
        root.right = root.tmp
        invertTree(root.left)
        invertTree(root.right)
        return rtype